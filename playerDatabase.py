import draftPredictor
import numpy
import webScraper

training_2007 = numpy.array(
    [draftPredictor.Player(3, 15.7, 9.6, 0.7, .616, 0.55, 3.3, 840, 656, 51, 40, 130, 0, 0),
     draftPredictor.Player(2, 25.8, 11.1, 1.3, .473, 1.9, 1.9, 19121, 5031, 2729, 840, 738,
                           12, 10),
     draftPredictor.Player(3, 10.3, 7.9, 1.7, .586, 0.8, 1.7, 9240, 5609, 1296, 434, 783, 5,
                           1),
     draftPredictor.Player(1, 11.3, 3.4, 6.1, .518, 2.23, 0.26, 10050, 2061, 4011, 1057, 137,
                           1, 0),
     draftPredictor.Player(2, 13.1, 6.5, 3.1, .488, 0.90, 1.2, 8314, 2885, 958, 461, 353, 0,
                           0),
     draftPredictor.Player(2, 11.3, 4.3, 2.8, .480, 1.6, 0.41, 6561, 2049, 1144, 908, 201, 0,
                           0),
     draftPredictor.Player(2, 14.7, 2.2, 1.0, .646, .97, 1.8, 2608, 1299, 161, 157, 265, 0,
                           0),
     draftPredictor.Player(3, 10.5, 6.4, 1.7, .616, .88, 1.7, 5557, 5790, 1087, 511, 840, 2,
                           1),
     draftPredictor.Player(3, 14.9, 6.4, 1.9, .532, 0.52, 1.7, 5932, 3893, 1271, 362, 652, 0,
                           0),
     draftPredictor.Player(1, 13.7, 3.1, 4.5, .466, 1.3, 0.02, 725, 195, 309, 83, 4, 0, 0),
     draftPredictor.Player(2, 14.4, 4.9, 2.0, .478, 1.3, 0.39, 9871, 4328, 1182, 1079, 305,
                           0, 0),
     draftPredictor.Player(2, 10.4, 6.3, 2.0, .555, 1.2, 1.3, 907, 531, 182, 132, 69, 0, 0),
     draftPredictor.Player(2, 12.3, 5.2, 0.7, .528, 0.83, 0.60, 3572, 1233, 353, 185, 142, 0, 0),
     draftPredictor.Player(1, 22.4, 4.7, 4.8, .472, 2.3, 0.29, 8185, 1912, 2333, 568, 94, 0, 0),
     draftPredictor.Player(1, 15.5, 5.1, 1.4, .484, 0.83, 0.27, 7604, 1301, 649, 356, 127, 0, 0),
     draftPredictor.Player(2, 12.9, 7.1, 1.2, .445, 0.69, 1.5, 7215, 2816, 925, 386, 342, 0, 0),
     draftPredictor.Player(2, 15.1, 3.5, 1.0, .492, 0.74, 0.55, 840, 656, 46, 12, 12, 4, 0),
     draftPredictor.Player(1, 13.1, 3.5, 4.1, .430, 1.1, 0.14, 6184, 1062, 1095, 353, 87, 0, 0),
     draftPredictor.Player(1, 14.8, 3.5, 1.9, .457, 0.62, 0.19, 8019, 2110, 1356, 337, 132, 0, 0),
     draftPredictor.Player(3, 5.5, 4.2, 0.6, .577, 0.61, 2.8, 581, 472, 47, 47, 162, 0, 0),
     draftPredictor.Player(1, 14.4, 3.7, 5.8, .450, 2.0, 0.06, 595, 276, 201, 59, 8, 0, 0),
     draftPredictor.Player(3, 14.7, 7.9, 2.0, .548, 0.54, 1.7, 3599, 1970, 425, 202, 388, 0, 0),
     draftPredictor.Player(1, 9.8, 4.3, 1.0, .445, 0.72, 0.26, 2114, 703, 243, 120, 48, 0, 0),
     draftPredictor.Player(2, 15.9, 7.2, 3.0, .504, 1.4, 0.28, 6120, 2527, 1200, 634, 136, 0, 0),
     webScraper.get_data('https://www.basketball-reference.com/players/t/tuckeal02.html', 2, 0, 0),
     webScraper.get_data('https://www.basketball-reference.com/players/l/landrca01.html', 2, 0, 0),
     webScraper.get_data('https://www.basketball-reference.com/players/p/pruitga01.html', 1, 0, 0),
     webScraper.get_data('https://www.basketball-reference.com/players/w/willima04.html', 2, 0, 0),
     webScraper.get_data('https://www.basketball-reference.com/players/f/fazekni01.html', 2, 0, 0),
     webScraper.get_data('https://www.basketball-reference.com/players/d/davisgl01.html', 2, 0, 0),
     webScraper.get_data('https://www.basketball-reference.com/players/d/davidje01.html', 2, 0, 0),
     webScraper.get_data('https://www.basketball-reference.com/players/m/mcrobjo01.html', 2, 0, 0)])
draftPredictor.Player(1, 15.7, 9.6, 0.7, .616, 3.3, 0.55, 840, 656, 51, 130, 40, 0, 0)
draftPredictor.Player(1, 15.7, 9.6, 0.7, .616, 3.3, 0.55, 840, 656, 51, 130, 40, 0, 0)
draftPredictor.Player(1, 15.7, 9.6, 0.7, .616, 3.3, 0.55, 840, 656, 51, 130, 40, 0, 0)
draftPredictor.Player(1, 15.7, 9.6, 0.7, .616, 3.3, 0.55, 840, 656, 51, 130, 40, 0, 0)
