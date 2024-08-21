
import sys

sys.path.append(r"../../../ECJ2SRbench/ECJ2SRbench/ECJwrapper")

import ECJregressor

hyper_params = [
    {}
]

est = ECJregressor(num_generations = 200,
                   population_size = 100,
                   max_program_size = 50,
                   min_program_size = 1,
                   num_registers = 8
                   )


def complexity(est):
    return est.get_model_complexity()


def model(est):
    return est.get_model_str()


eval_kwargs = {}
