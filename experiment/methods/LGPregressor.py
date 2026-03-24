"""an interface for the actual LGPregressor module. SRBench calls this module to run the LGPregressor symbolic regression method. The actual LGPregressor module is located in ../LGPregressor/LGPregressor.py, and this file is used to call the LGPregressor module and run the symbolic regression method."""

import sys
import os

sys.path.append(os.path.abspath("../../LGPregressor"))


from LGPregressor import LGPregressor

hyper_params = [
    {}
]

est = LGPregressor(num_generations = -1,
                   population_size = -1,
                   max_program_size = -1,
                   min_program_size = -1
                   )


def complexity(est):
    return est.get_model_complexity()


def model(est):
    return est.get_model_str()


eval_kwargs = {}