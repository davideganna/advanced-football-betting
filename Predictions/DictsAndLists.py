# ------------------------------- dicts_and_lists.py ------------------------------- #
# Contains a collection of Lists and Dictionaries used throughout the program.
# ---------------------------------------------------------------------------------- #
import numpy as np


# Last away and home game indexes.
# [0] is home index, [1] is away index 
last_home_away_index_dict = {
    'Alaves' : [None, None], 
    'Arsenal' : [None, None], 
    'Aston Villa' : [None, None], 
    'Atalanta' : [None, None], 
    'Ath Bilbao' : [None, None], 
    'Ath Madrid' : [None, None], 
    'Augsburg' : [None, None], 
    'Barcelona' : [None, None], 
    'Bayern Munich' : [None, None], 
    'Benevento' : [None, None], 
    'Betis' : [None, None], 
    'Bielefeld' : [None, None], 
    'Bologna' : [None, None], 
    'Bournemouth' : [None, None], 
    'Brescia' : [None, None], 
    'Brighton' : [None, None], 
    'Burnley' : [None, None], 
    'Cadiz' : [None, None], 
    'Cagliari' : [None, None], 
    'Cardiff' : [None, None], 
    'Celta' : [None, None], 
    'Chelsea' : [None, None], 
    'Chievo' : [None, None], 
    'Crotone' : [None, None], 
    'Crystal Palace' : [None, None], 
    'Darmstadt' : [None, None], 
    'Dortmund' : [None, None], 
    'Eibar' : [None, None], 
    'Ein Frankfurt' : [None, None], 
    'Elche' : [None, None], 
    'Empoli' : [None, None], 
    'Espanol' : [None, None], 
    'Everton' : [None, None], 
    'FC Koln' : [None, None], 
    'Fiorentina' : [None, None], 
    'Fortuna Dusseldorf' : [None, None], 
    'Freiburg' : [None, None], 
    'Frosinone' : [None, None], 
    'Fulham' : [None, None], 
    'Genoa' : [None, None], 
    'Getafe' : [None, None], 
    'Girona' : [None, None], 
    'Granada' : [None, None], 
    'Hamburg' : [None, None], 
    'Hannover' : [None, None], 
    'Hertha' : [None, None], 
    'Hoffenheim' : [None, None], 
    'Huddersfield' : [None, None], 
    'Huesca' : [None, None], 
    'Hull' : [None, None], 
    'Ingolstadt' : [None, None], 
    'Inter' : [None, None], 
    'Juventus' : [None, None], 
    'La Coruna' : [None, None], 
    'Las Palmas' : [None, None], 
    'Lazio' : [None, None], 
    'Lecce' : [None, None], 
    'Leeds' : [None, None], 
    'Leganes' : [None, None], 
    'Leicester' : [None, None], 
    'Levante' : [None, None], 
    'Leverkusen' : [None, None], 
    'Liverpool' : [None, None], 
    "M'gladbach" : [None, None], 
    'Mainz' : [None, None], 
    'Malaga' : [None, None], 
    'Mallorca' : [None, None], 
    'Man City' : [None, None], 
    'Man United' : [None, None], 
    'Middlesbrough' : [None, None], 
    'Milan' : [None, None], 
    'Napoli' : [None, None], 
    'Newcastle' : [None, None], 
    'Norwich' : [None, None], 
    'Nurnberg' : [None, None], 
    'Osasuna' : [None, None], 
    'Paderborn' : [None, None], 
    'Palermo' : [None, None], 
    'Parma' : [None, None], 
    'Pescara' : [None, None], 
    'RB Leipzig' : [None, None], 
    'Real Madrid' : [None, None], 
    'Roma' : [None, None], 
    'Salernitana' : [None, None],
    'Sampdoria' : [None, None], 
    'Sassuolo' : [None, None], 
    'Schalke 04' : [None, None], 
    'Sevilla' : [None, None], 
    'Sheffield United' : [None, None], 
    'Sociedad' : [None, None], 
    'Southampton' : [None, None], 
    'Sp Gijon' : [None, None], 
    'Spal' : [None, None], 
    'Spezia' : [None, None], 
    'Stoke' : [None, None], 
    'Stuttgart' : [None, None], 
    'Sunderland' : [None, None], 
    'Swansea' : [None, None], 
    'Torino' : [None, None], 
    'Tottenham' : [None, None], 
    'Udinese' : [None, None], 
    'Union Berlin' : [None, None], 
    'Valencia' : [None, None], 
    'Valladolid' : [None, None], 
    'Vallecano' : [None, None], 
    'Verona' : [None, None], 
    'Villarreal' : [None, None],
    'Watford' : [None, None], 
    'Werder Bremen' : [None, None], 
    'West Brom' : [None, None], 
    'West Ham' : [None, None], 
    'Wolfsburg' : [None, None], 
    'Wolves' : [None, None]
}

teams_to_int = {
    'Alaves' : 0, 
    'Arsenal' : 1, 
    'Aston Villa' : 2, 
    'Atalanta' : 3, 
    'Ath Bilbao' : 4, 
    'Ath Madrid' : 5, 
    'Augsburg' : 6, 
    'Barcelona' : 7,
    'Bayern Munich' : 8, 
    'Benevento' : 9, 
    'Betis' : 10, 
    'Bielefeld' : 11, 
    'Bologna' : 12, 
    'Bournemouth' : 13, 
    'Brescia' : 14, 
    'Brighton' : 15, 
    'Burnley' : 16, 
    'Cadiz' : 17, 
    'Cagliari' : 18, 
    'Cardiff' : 19, 
    'Celta' : 20, 
    'Chelsea' : 21, 
    'Chievo' : 22, 
    'Crotone' : 23, 
    'Crystal Palace' : 24, 
    'Darmstadt' : 25, 
    'Dortmund' : 26, 
    'Eibar' : 27, 
    'Ein Frankfurt' : 28, 
    'Elche' : 29, 
    'Empoli' : 30, 
    'Espanol' : 31, 
    'Everton' : 32, 
    'FC Koln' : 33, 
    'Fiorentina' : 34, 
    'Fortuna Dusseldorf' : 35, 
    'Freiburg' : 36, 
    'Frosinone' : 37, 
    'Fulham' : 38, 
    'Genoa' : 39, 
    'Getafe' : 40, 
    'Girona' : 41, 
    'Granada' : 42, 
    'Hamburg' : 43, 
    'Hannover' : 44, 
    'Hertha' : 45, 
    'Hoffenheim' : 46, 
    'Huddersfield' : 47, 
    'Huesca' : 48, 
    'Hull' : 49, 
    'Ingolstadt' : 50, 
    'Inter' : 51, 
    'Juventus' : 52, 
    'La Coruna' : 53, 
    'Las Palmas' : 54, 
    'Lazio' : 55, 
    'Lecce' : 56, 
    'Leeds' : 57, 
    'Leganes' : 58, 
    'Leicester' : 59, 
    'Levante' : 60, 
    'Leverkusen' : 61, 
    'Liverpool' : 62, 
    "M'gladbach" : 63, 
    'Mainz' : 64, 
    'Malaga' : 65, 
    'Mallorca' : 66, 
    'Man City' : 67, 
    'Man United' : 68, 
    'Middlesbrough' : 69, 
    'Milan' : 70, 
    'Napoli' : 71, 
    'Newcastle' : 72, 
    'Norwich' : 73, 
    'Nurnberg' : 74, 
    'Osasuna' : 75, 
    'Paderborn' : 76, 
    'Palermo' : 77, 
    'Parma' : 78, 
    'Pescara' : 79, 
    'RB Leipzig' : 80, 
    'Real Madrid' : 81, 
    'Roma' : 82, 
    'Salernitana' : 83,
    'Sampdoria' : 84, 
    'Sassuolo' : 85, 
    'Schalke 04' : 86, 
    'Sevilla' : 87, 
    'Sheffield United' : 88, 
    'Sociedad' : 89, 
    'Southampton' : 90, 
    'Sp Gijon' : 91, 
    'Spal' : 92, 
    'Spezia' : 93, 
    'Stoke' : 94, 
    'Stuttgart' : 95, 
    'Sunderland' : 96, 
    'Swansea' : 97, 
    'Torino' : 98, 
    'Tottenham' : 99, 
    'Udinese' : 100, 
    'Union Berlin' : 101, 
    'Valencia' : 102, 
    'Valladolid' : 103, 
    'Vallecano' : 104, 
    'Verona' : 105, 
    'Villarreal' : 106,
    'Watford' : 107, 
    'Werder Bremen' : 108, 
    'West Brom' : 109, 
    'West Ham' : 110, 
    'Wolfsburg' : 111, 
    'Wolves' : 112
}