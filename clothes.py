def verify_breast_size(size_in_inch):
    if size_in_inch <= 31:
        return "s"
    elif size_in_inch <= 33:
        return "m"
    elif size_in_inch <= 36:
        return "l"
    else:
        return "xl"


def get_clothes_list_by_tier_and_breast_size(tier, breast_size):
    if tier == "green":
        if breast_size == "s":
            green_s = {"fullpe-s": ["longjacket-s", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "pe-s": ["longjacket-s", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "longshirt-green-s": ["longjacket-s", "longvest-s", "shortvestforlong-s", "longcoat-s",
                                             "longcoatwithvest-s", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "shortshirt-green-s": ["longjacket-s", "longvest-s", "shortvestforshort-s-s", "longcoat-s",
                                              "longcoatwithvest-s", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "uniform-green-s": ["longjacket-s", "longvest-s", "longcoat-s",
                                           "longcoatwithvest-s", "uniformvest-s", "longscarf-1", "longscarf-2",
                                           "scarf-1", "scarf-2"]
                       }

            return green_s
        elif breast_size == "m":
            green_m = {"fullpe-m": ["longjacket-m", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "pe-m": ["longjacket-m", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "longshirt-green-m": ["longjacket-m", "longvest-m", "shortvestforlong-m", "longcoat-m",
                                             "longcoatwithvest-m", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "shortshirt-green-m": ["longjacket-m", "longvest-m", "shortvestforshort-m-m", "longcoat-m",
                                              "longcoatwithvest-m", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "uniform-green-m": ["longjacket-m", "longvest-m", "longcoat-m",
                                           "longcoatwithvest-m", "uniformvest-m", "longscarf-1", "longscarf-2",
                                           "scarf-1", "scarf-2"]
                       }

            return green_m
        elif breast_size == "l":
            green_l = {"fullpe-l": ["longjacket-l", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "pe-l": ["longjacket-l", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "longshirt-green-l": ["longjacket-l", "longvest-l", "shortvestforlong-l", "longcoat-l",
                                             "longcoatwithvest-l", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "shortshirt-green-l": ["longjacket-l", "longvest-l", "shortvestforshort-l-l", "longcoat-l",
                                              "longcoatwithvest-l", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                       "uniform-green-l": ["longjacket-l", "longvest-l", "longcoat-l",
                                           "longcoatwithvest-l", "uniformvest-l", "longscarf-1", "longscarf-2",
                                           "scarf-1", "scarf-2"]
                       }

            return green_l
        elif breast_size == "xl":
            green_xl = {"fullpe-xl": ["longjacket-xl", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],

                        "shortshirt-green-xl": ["longjacket-xl", "longvest-xl", "shortvestforshort-xl-xl",
                                                "longcoat-xl",
                                                "longcoatwithvest-xl", "longscarf-1", "longscarf-2", "scarf-1",
                                                "scarf-2"],
                        "uniform-green-xl": ["longjacket-xl", "longvest-xl", "longcoat-xl",
                                             "longcoatwithvest-xl", "uniformvest-xl", "longscarf-1", "longscarf-2",
                                             "scarf-1", "scarf-2"]
                        }

            return green_xl
    elif tier == "purple":
        if breast_size == "s":
            purple_s = {"fullpe-s": ["longjacket-s", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "pe-s": ["longjacket-s", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "longshirt-purple-s": ["longjacket-s", "longvest-s", "shortvestforlong-s", "longcoat-s",
                                               "longcoatwithvest-s", "longscarf-1", "longscarf-2", "scarf-1",
                                               "scarf-2"],
                        "shortshirt-purple-s": ["longjacket-s", "longvest-s", "shortvestforshort-s-s", "longcoat-s",
                                                "longcoatwithvest-s", "longscarf-1", "longscarf-2", "scarf-1",
                                                "scarf-2"],
                        "uniform-purple-s": ["longjacket-s", "longvest-s", "longcoat-s",
                                             "longcoatwithvest-s", "uniformvest-s", "longscarf-1", "longscarf-2",
                                             "scarf-1", "scarf-2"],
                        "basketball-s": ["longjacket-s", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "football-s": ["longjacket-s", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "swimming-s": ["longjacket-s", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        }
            return purple_s
        elif breast_size == "m":
            purple_m = {"fullpe-m": ["longjacket-m", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "pe-m": ["longjacket-m", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "longshirt-purple-m": ["longjacket-m", "longvest-m", "shortvestforlong-m", "longcoat-m",
                                               "longcoatwithvest-m", "longscarf-1", "longscarf-2", "scarf-1",
                                               "scarf-2"],
                        "shortshirt-purple-m": ["longjacket-m", "longvest-m", "shortvestforshort-m-m", "longcoat-m",
                                                "longcoatwithvest-m", "longscarf-1", "longscarf-2", "scarf-1",
                                                "scarf-2"],
                        "uniform-purple-m": ["longjacket-m", "longvest-m", "longcoat-m",
                                             "longcoatwithvest-m", "uniformvest-m", "longscarf-1", "longscarf-2",
                                             "scarf-1", "scarf-2"],
                        "basketball-m": ["longjacket-m", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "football-m": ["longjacket-m", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "swimming-m": ["longjacket-m", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        }
            return purple_m
        elif breast_size == "l":
            purple_l = {"fullpe-l": ["longjacket-l", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "pe-l": ["longjacket-l", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "longshirt-purple-l": ["longjacket-l", "longvest-l", "shortvestforlong-l", "longcoat-l",
                                               "longcoatwithvest-l", "longscarf-1", "longscarf-2", "scarf-1",
                                               "scarf-2"],
                        "shortshirt-purple-l": ["longjacket-l", "longvest-l", "shortvestforshort-l-l", "longcoat-l",
                                                "longcoatwithvest-l", "longscarf-1", "longscarf-2", "scarf-1",
                                                "scarf-2"],
                        "uniform-purple-l": ["longjacket-l", "longvest-l", "longcoat-l",
                                             "longcoatwithvest-l", "uniformvest-l", "longscarf-1", "longscarf-2",
                                             "scarf-1", "scarf-2"],
                        "basketball-l": ["longjacket-l", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "football-l": ["longjacket-l", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        "swimming-l": ["longjacket-l", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                        }
            return purple_l
        elif breast_size == "xl":
            purple_xl = {"fullpe-xl": ["longjacket-xl", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                         "shortshirt-purple-xl": ["longjacket-xl", "longvest-xl", "shortvestforshort-xl-xl",
                                                  "longcoat-xl",
                                                  "longcoatwithvest-xl", "longscarf-1", "longscarf-2", "scarf-1",
                                                  "scarf-2"],
                         "uniform-purple-xl": ["longjacket-xl", "longvest-xl", "longcoat-xl",
                                               "longcoatwithvest-xl", "uniformvest-xl", "longscarf-1", "longscarf-2",
                                               "scarf-1", "scarf-2"],
                         "swimming-xl": ["longjacket-xl", "longscarf-1", "longscarf-2", "scarf-1", "scarf-2"],
                         }
            return purple_xl
