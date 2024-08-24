
import sys
import os

sys.path.append(os.path.abspath("../../ECJ2SRbench/ECJ2SRbench/ECJwrapper"))

# print(20*"=" + " sys.path " + 20*"=")
# for p in sys.path:
#     print(p)
# print(50*"=")

from ECJregressor import ECJregressor

hyper_params = [
    {}
]

est = ECJregressor(num_generations = 250,
                   population_size = 500,
                   max_program_size = 50,
                   min_program_size = 1,
                   num_registers = 8
                   )


def complexity(est):
    return est.get_model_complexity()


def model(est):
    return est.get_model_str()


eval_kwargs = {}
