import argparse

from src import service, sample_evaluation

def main():
    parser = argparse.ArgumentParser(description='Interview script')

    # If nothing provided, service will work
    parser.add_argument('--mode', choices=['service', 'sample'], default='service',
                        help='service or sample mode')

    args = parser.parse_args()

    if args.mode == 'service':
        service.main()
    elif args.mode == 'sample':
        sample_evaluation.main()

if __name__ == '__main__':
    main()