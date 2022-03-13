import multiprocessing
import random

from clothes import *
from pilutil import *


# steps:
# 0. todo: write another script to generate a json of random tier, set of names, position(purple only), class number, interest, 3size, skin colour, isMimi(5%)
# 1. input: tier = "green"/"purple", breast_size = int (done)
# 2. todo: get tier, breast_size, skin colour, isMimi(5%) from the json
# 3. verify if the breast_size is s/m/l/xl
# 4. get clothes-jacket hash-map with breast_size and tier
# 5. get all the layer images
# 6. randomize the colour of the layers (multiprocessing as it was so slow!)
# 7. combine all the layers
# 8. save the image and json, done!

def generate(tier, size_in_inch):
    is_ahoge = bool(random.getrandbits(1))
    is_mimi = bool(random.getrandbits(1))
    is_jacket = bool(random.getrandbits(1))

    # multiprocessing with 50% cpu
    pool = multiprocessing.Pool(max(multiprocessing.cpu_count() // 2, 1))
    manager = multiprocessing.Manager()
    result_dict = manager.dict()

    start_time = time.time()
    print('start')

    ####################
    # 3. verify if the breast_size is s/m/l/xl
    ####################
    breast_size = verify_breast_size(size_in_inch)
    print("size_in_inch: " + str(size_in_inch) + ", breast_size: " + breast_size)
    print("tier: " + tier)

    ####################
    # 4. get clothes-jacket hash-map with breast_size and tier
    ####################
    clothes_dict = get_clothes_list_by_tier_and_breast_size(tier, breast_size)
    # print(clothes_dict.values())
    this_clothes = random.choice(list(clothes_dict.keys()))

    ####################
    # 5. get all the layer images
    ####################
    bgColour_name = random.choice(os.listdir("image/0_bgc/"))
    bgColour = Image.open("image/0_bgc/" + bgColour_name)

    bgPic_optional_name = random.choice(os.listdir("image/1_bgpic_optional/"))
    bgPic_optional = Image.open("image/1_bgpic_optional/" + bgPic_optional_name)

    backHair_name = random.choice(os.listdir("image/2_back_hair/"))
    backHair = Image.open("image/2_back_hair/" + backHair_name)

    body_name = random.choice(os.listdir("image/3_rawbody/"))
    body = Image.open("image/3_rawbody/" + body_name)

    clothes_name = this_clothes + ".png"
    clothes = Image.open("image/4_clothes-" + tier + "/" + clothes_name)

    brow_name = random.choice(os.listdir("image/5_brow/"))
    brow = Image.open("image/5_brow/" + brow_name)

    eyes_name = random.choice(os.listdir("image/6_eye/"))
    eyes = Image.open("image/6_eye/" + eyes_name)

    nose_name = random.choice(os.listdir("image/7_nose/"))
    nose = Image.open("image/7_nose/" + nose_name)

    frontHair_name = random.choice(os.listdir("image/10_front/"))
    frontHair = Image.open("image/10_front/" + frontHair_name)

    mouth_name = random.choice(os.listdir("image/8_mouth/"))
    mouth = Image.open("image/8_mouth/" + mouth_name)

    shinyHair = Image.open("image/12_shinyhair.png")

    accessory_optional_name = random.choice(os.listdir("image/13_accessory_optional/"))
    accessory_optional = Image.open(
        "image/13_accessory_optional/" + accessory_optional_name)

    ####################
    # 6. randomize the colour of the layers (multiprocessing as it was so slow!)
    ####################
    hue = random.randint(0, 360)
    s = random.uniform(0.4, 1.05)
    # colouredBg = colorize(bgColour, bgHue, 1, s)
    pool.apply_async(multiprocess_colorize, args=(bgColour, hue, 1, s, result_dict, "colouredBg"))

    hue = random.randint(0, 360)
    b = random.uniform(1, 1.5)
    s = random.uniform(0.4, 1.05)
    # coloredEyes = colorize(eyes, eyesHue, b, s)
    pool.apply_async(multiprocess_colorize, args=(eyes, hue, b, s, result_dict, "coloredEyes"))

    hue = random.randint(0, 360)
    b = random.uniform(0.5, 1.5)
    s = random.uniform(0.4, 1.5)
    # coloredBackHair = colorize(backHair, hairHue, b, s)
    # coloredFrontHair = colorize(frontHair, hairHue, b, s)
    # colouredBrow = colorize(brow, hairHue, b, s)
    # colouredAhoge = colorize(ahoge, hairHue, b, s)
    # colouredMimi = colorize(mimi, hairHue, b, s)
    pool.apply_async(multiprocess_colorize,
                     args=(backHair, hue, b, s, result_dict, "coloredBackHair"))
    pool.apply_async(multiprocess_colorize,
                     args=(frontHair, hue, b, s, result_dict, "coloredFrontHair"))
    pool.apply_async(multiprocess_colorize, args=(brow, hue, b, s, result_dict, "colouredBrow"))

    ahoge_name = ""
    if is_ahoge:
        ahoge_name = random.choice(os.listdir("image/11_ahoge/"))
        ahoge = Image.open("image/11_ahoge/" + ahoge_name)
        pool.apply_async(multiprocess_colorize, args=(ahoge, hue, b, s, result_dict, "colouredAhoge"))

    mimi_name = ""
    if is_mimi:
        mimi_name = random.choice(os.listdir("image/11_mimi/"))
        mimi = Image.open("image/11_mimi/" + mimi_name)
        pool.apply_async(multiprocess_colorize, args=(mimi, hue, b, s, result_dict, "colouredMimi"))

    jacket_optional_name = ""
    if is_jacket:
        jacket_list = clothes_dict.get(this_clothes)
        this_jacket = random.choice(jacket_list)
        jacket_optional_name = this_jacket + ".png"
        jacket_optional = Image.open("image/9_jacket_optional/" + jacket_optional_name)
        hue = random.randint(0, 360)
        b = random.uniform(0.5, 1.5)
        s = random.uniform(0.4, 1.2)
        # colouredJacket = colorize(jacket_optional, jacketHue, b, s)
        pool.apply_async(multiprocess_colorize,
                         args=(jacket_optional, hue, b, s, result_dict, "colouredJacket"))

    hue = random.randint(0, 360)
    b = random.uniform(0.5, 1.2)
    s = random.uniform(0.4, 1.3)
    # colouredAccessory = colorize(accessory_optional, accessoryHue, b, s)
    if accessory_optional_name.split(".")[0].split("-").pop() == "f":
        print("fixed-colour accessory")
        result_dict["colouredAccessory"] = accessory_optional
    else:
        pool.apply_async(multiprocess_colorize,
                         args=(accessory_optional, hue, b, s, result_dict, "colouredAccessory"))

    pool.close()
    pool.join()

    colouredBg = result_dict.get("colouredBg")
    coloredBackHair = result_dict.get("coloredBackHair")
    colouredBrow = result_dict.get("colouredBrow")
    coloredEyes = result_dict.get("coloredEyes")
    colouredJacket = result_dict.get("colouredJacket")
    coloredFrontHair = result_dict.get("coloredFrontHair")
    colouredAhoge = result_dict.get("colouredAhoge")
    colouredMimi = result_dict.get("colouredMimi")
    colouredAccessory = result_dict.get("colouredAccessory")

    ####################
    # 7. combine all the layers
    ####################
    resultPicWithBg = colouredBg
    resultPic = coloredBackHair

    resultPic.paste(body, (0, 0), body)
    resultPic.paste(clothes, (0, 0), clothes)
    resultPic.paste(colouredBrow, (0, 0), colouredBrow)
    resultPic.paste(coloredEyes, (0, 0), coloredEyes)
    resultPic.paste(nose, (0, 0), nose)
    if is_jacket:
        resultPic.paste(colouredJacket, (0, 0), colouredJacket)
    resultPic.paste(coloredFrontHair, (0, 0), coloredFrontHair)
    resultPic.paste(mouth, (0, 0), mouth)
    if is_ahoge:
        resultPic.paste(colouredAhoge, (0, 0), colouredAhoge)
    if is_mimi:
        resultPic.paste(colouredMimi, (0, 0), colouredMimi)
    resultPic.paste(shinyHair, (0, 0), shinyHair)
    resultPic.paste(colouredAccessory, (0, 0), colouredAccessory)

    if tier == "purple":
        resultPicWithBg.paste(bgPic_optional, (0, 0), bgPic_optional)
    resultPicWithBg.paste(resultPic, (0, 0), resultPic)

    ####################
    # 8. save the image and json, done!
    ####################
    resultPicWithBg.show()
    timeForFile = str(round(time.time() * 1000))
    resultPic.save("result/result" + timeForFile + ".png", "png")
    resultPicWithBg.save("result/result" + timeForFile + "_with_bg.png", "png")
    f = open("result/result" + timeForFile + "_content.json", "a")
    f.write('{\n')
    f.write('   "bgColour_name": "' + bgColour_name.split(".")[0] + '",\n')
    f.write('   "bgPic_optional_name": "' + bgPic_optional_name.split(".")[0] + '",\n')
    f.write('   "backHair_name": "' + backHair_name.split(".")[0] + '",\n')
    f.write('   "body_name": "' + body_name.split(".")[0] + '",\n')
    f.write('   "brow_name": "' + brow_name.split(".")[0] + '",\n')
    f.write('   "eyes_name": "' + eyes_name.split(".")[0] + '",\n')
    f.write('   "nose_name": "' + nose_name.split(".")[0] + '",\n')
    f.write('   "jacket_optional_name": "' + jacket_optional_name.split(".")[0] + '",\n')
    f.write('   "frontHair_name": "' + frontHair_name.split(".")[0] + '",\n')
    f.write('   "mouth_name": "' + mouth_name.split(".")[0] + '",\n')
    f.write('   "ahoge_name": "' + ahoge_name.split(".")[0] + '",\n')
    f.write('   "mimi_name": "' + mimi_name.split(".")[0] + '",\n')
    f.write('   "accessory_optional_name": "' + accessory_optional_name.split(".")[0] + '"\n')
    f.write('}')
    f.close()
    print("--- %s seconds ---" % (time.time() - start_time))


for x in range(1):
    if __name__ == '__main__':
        generate("purple", 37)
