from analysis.similarity import ImageAnalyzer
import os


def main():
    base_dir = os.getcwd()
    analyzer = ImageAnalyzer(base_dir)
    results = analyzer.analyze_images()

    for res in results:
        print(res['vector'])

    return res['vector']


if __name__ == "__main__":
    output = main()