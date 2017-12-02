import os
import tqdm
from multiprocessing import Pool
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--path_to_cases', default='/DDSM/cases', help='path to the cases dir containing normals, cancers, etc.')
parser.add_argument('--workers', type=int, default=4, help='Amount of parallell workers')

args = parser.parse_args()

all_dirs = []
for subcase_dir in os.listdir(args.path_to_cases):
    if subcase_dir == '.listing':
        continue
    subcase_path = os.path.join(args.path_to_cases, subcase_dir)
    for subcase_subdir in os.listdir(subcase_path):
        if subcase_subdir == '.listing':
            continue
        subcase_subdir_path = os.path.join(subcase_path, subcase_subdir)
        for case_dir in os.listdir(subcase_subdir_path):
            case_path = os.path.join(subcase_subdir_path, case_dir)
            all_dirs.append(case_path)

def job(args):
    ljpeg_path = args
    cmd = 'bash ddsm_ljpeg.sh -d "{0}"'.format(ljpeg_path)
    os.system(cmd)
    return None

print("Num dirs to convert {}".format(len(all_dirs)))
pool = Pool(args.workers)
for _ in tqdm.tqdm(pool.imap_unordered( job, all_dirs) , total=len(all_dirs)):
    pass

print('done')
