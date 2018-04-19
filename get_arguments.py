import argparse

logdir_path = './log'

def get_arguments():
    parser = argparse.ArgumentParser(description='Usage: python train1.py ./dataset/TIMIT')	
    parser.add_argument('TIMIT', type=str, help='non-free dataset TIMIT could be accessed at https://catalog.ldc.upenn.edu/ldc93s1 ')
    arguments = parser.parse_args()
    return arguments

if __name__ == '__main__':
    args = get_arguments()
    case = args.TIMIT
    print(case)
    logdir = '{}/{}/train1'.format(logdir_path, case)
#    print(logdir)
#    train(logdir=logdir)
#    print("Done")

