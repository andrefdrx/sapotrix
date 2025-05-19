from analysis.similarity import ImageAnalyzer
import os

if __name__ == "__main__":
    base_dir = os.getcwd()
    analyzer = ImageAnalyzer(base_dir)
    analyzer.analyze_images()
