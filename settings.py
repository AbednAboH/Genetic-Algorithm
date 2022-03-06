from sys import maxsize

# selectors aliases
RAND,SUS,RWS,RANK=0,1,2,3

# fitness function aliases / "function selectors"
DISTANCE,BUL_PGIA=0,1

# type of cross function
CROSS1,CROSS2,UNI_CROSS=1,2,3

# penalties given by bul pgiaa heuristic

PENALTY = 30
HIGH_PENALTY = 90

# population settings
GA_POPSIZE = 2048
GA_MAXITER = 16384
GA_ELITRATE = 0.10
GA_MUTATIONRATE = 0.25
GA_MUTATION = maxsize * GA_MUTATIONRATE
GA_TARGET = "hello World!"
TAR_size = len(GA_TARGET)