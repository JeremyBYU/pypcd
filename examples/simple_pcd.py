from pypcd.pypcd import PointCloud

PCD_FILE = "test_data/pc_01.pcd"

def main():
    a = PointCloud.from_path(PCD_FILE)
    print(a.pc_data['x'])

if __name__ == "__main__":
    main()