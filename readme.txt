http://127.0.0.1:8080/easynas/test
http://192.168.80.128:8080/easynas/test

git clone https://github.com/fanzi2009/easynas.git

cd easynas/middleware
./create_zfs.py pool1 stripe ad1 ad3
./create_zfs.py pool1 mirror ad1 ad3
./create_zfs.py pool1 raidz ad1 ad3
./destroy_zfs.py pool1
