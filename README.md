# TXT to JSON

> When im working on dictionary project (utf8 txt format), i found dataset that need for system it is in .txt format and i convert that into .json with python algorithm.

# .txt file format example

    a=අනියමාර්ථ විශේෂණය, ඉංග්‍රීසි හෝඩියේ මුල් අකුර
    abaca=පිලිපීනයේ ගසක  විශේෂයක්

# .json file after convert

    [
        {
            "word": "a",
            "options": "අනියමාර්ථ විශේෂණය, ඉංග්‍රීසි හෝඩියේ මුල් අකුර"
        },
        {
            "word": "abaca",
            "options": "පිලිපීනයේ ගසක  විශේෂයක්"
        }
    ]
