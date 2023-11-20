import os 
from zeroshot import randomPrime1 as zsRP1, randomPrime2 as zsRP2
from oneshotRSA import osRandomPrime1 as osRP1, osRandomPrime2 as osRP2
from fewshotCoT import randomPrime1 as fsCOTRP1
from zeroshot.llama2 import randomPrime2 as zsLLRP2
import tqdm
from time import sleep
import time

NUM_PRIME_GEN = 10_000
PRIME_GENERATORS = [
    zsRP1,
    zsRP2,
    fsCOTRP1,
    osRP1,
    # osRP2 # couldn't find any prime in reasonable time
]


def find_duplicate_num(keys, filepath, time_perf):
    isExist = os.path.exists(filepath)
    if not isExist:
        os.makedirs(filepath)
    map = dict()
    duplicates = set()
    total_keys = len(keys)  
    dup_counter = 0
    for key in tqdm.tqdm(keys):
        if key in map:
            map[key] += 1
            duplicates.add(key)
            dup_counter += 1
        else:
            map[key] = 1
    print(f'Percentage of duplicates {(dup_counter/total_keys)*100}%')
    with open(f'{filepath}/duplicates.txt', 'w') as f: 
        f.write("\n".join([str(key) for key in duplicates]))
    with open(f'{filepath}/percentage', 'w') as f:
        f.write(str((dup_counter/total_keys)*100))
    with open(f'{filepath}/time_perf', 'w') as f:
        f.write(str(time_perf))
    with open(f'{filepath}/keys', 'w') as f:
        f.write("\n".join([str(key) for key in keys]))
    return duplicates


print(f'Starting Program')


if __name__ == "__main__":

    print(f'Generating for {zsLLRP2.__name__}')
    start = time.time()
    keys = [zsLLRP2.get_random_prime_number(2**16) for _ in tqdm.tqdm(range(NUM_PRIME_GEN))]
    end = time.time()
    print(f'Checking duplicates for {zsLLRP2.__name__}')
    duplicates = find_duplicate_num(keys, 'generatedKeys/llama2' + zsLLRP2.__name__.replace(".", ""), end-start)
    print(f'Duplicates found {len(duplicates)} for {zsLLRP2.__name__}')
    print(duplicates)
    del keys 
    del duplicates
    sleep(10)
    print(f'+'* 80)
    print(f'-'*80)
    

    print(f'Starting Program')
    for generator in PRIME_GENERATORS:
        print(f'Generating for {generator.__name__}')
        start = time.time()
        keys = [generator.get_random_prime_number() for _ in tqdm.tqdm(range(NUM_PRIME_GEN))]
        end = time.time()
        print(f'Checking duplicates for {generator.__name__}')
        duplicates = find_duplicate_num(keys, 'generatedKeys/' + generator.__name__.replace(".", ""), end-start)
        print(f'Duplicates found {len(duplicates)} for {generator.__name__}')
        print(duplicates)
        del keys 
        del duplicates
        sleep(10)
        print(f'+'* 80)
        print(f'-'*80)

