import argparse
from src import service
from src import sample_evaluation

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Interview script')

    # Add mode argument
    parser.add_argument('--mode', choices=['service', 'sample'], default='service',
                        help='Specify the mode (service or sample)')

    # Parse command-line arguments
    args = parser.parse_args()

    # Execute behavior based on mode
    if args.mode == 'service':
        service.main()
    elif args.mode == 'sample':
        sample_evaluation.main()

if __name__ == '__main__':
    main()