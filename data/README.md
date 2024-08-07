# Dataset generation

To download the dataset follow instructions in the main README.

Here we outline the dataset generation process. More details are available in the paper.

## Sequence generation

### [ReplicaCAD](https://aihabitat.org/datasets/replica_cad/)

The ReplicaCAD dataset is an artist's recreation of the FRL appartment with many different room configurations. 

We generated 6 sequences by simulating a locobot moving through two different apartment configurations. There are three types of sequences we generate for each apartment configuration. One navigation sequence (nav), one object reconstruction sequence (obj) and one manipulation sequence (mnp).

To generate the sequences, first install [Habitat-Sim](https://github.com/facebookresearch/habitat-sim). Then the sequences can be generated by running this [script](https://drive.google.com/file/d/15ZLZQ5KNvb-jdhTAXrgkHRzOLGcMSCnW/view?usp=sharing)

### [ScanNet](http://www.scan-net.org/)

For the ScanNet dataset, we use 6 sequenes. These can be obtained by downloading the ScanNet dataset and exporting the sequences with [this script](https://github.com/ScanNet/ScanNet/tree/master/SensReader/python).

We use 3 longer and 3 shorter randomly chosen ScanNet sequences. 

Longer:
scene0010_00: 6.52m
scene0030_00: 6.98m
scene0031_00: 7.66m
Shorter:
scene0004_00: 9.55m
scene0005_00: 5.40m
scene0009_00: 7.00m

### [Tabletop dataset](https://drive.google.com/file/d/1tncMjkFLNlCZztTHwhO6Hn6EoEevGBDL/view?usp=sharing)

The tabletop dataset consists of 5 short trajectories we collect on the Franka mounted with a Realsense camera. We scan an assortment of [YCB](https://www.ycbbenchmarks.com/object-set/) objects and a 3D printed [Stanford bunny](http://graphics.stanford.edu/data/3Dscanrep/).

## Ground truth SDF generation

The sequences are accompanied by ground truth SDF voxel grids with a voxel size of 1cm.

### ReplicaCAD

We generate the full SDF by composing the SDF for the stage (empty room) and all objects in the scene. 

First, we use habitat-sim to generate the SDF for the stage.

To generate an SDF run:
```
cd coordModels
python datasets/replicaCAD.py
```

### ScanNet

When building habitat-sim from source, be sure to use the `vhacd` flag:
```
python setup.py install --vhacd --bullet --with-cuda
```

Stage SDF is generated by pressing y in habitat c++ viewer. 
For Replica-CAD, use `m_dim = 1300` for 1cm voxel size and `mdim = 512` for 2.5cm voxel size.

To open the viewer run with `apt_3`: 
```
./build/viewer --dataset /path/to/replica_cad/replicaCAD.scene_dataset_config.json --enable-physics -- apt_3
```
Then press the y key to save the stage SDF. You must create a directory `sdf` first. It will save a `sdf.txt` and `transform.txt` file.

Then create directory in habitat-sdfs for the sequence, with the `sdf.txt` and `transform.txt` files. Run the script `coordModels/dataset/examples/scannet.py` with the correct sequence name passed.

Then to load a scene into viewer, run:
```
./build/viewer  --enable-physics -- /mnt/sda/ScanNet/scans/scene0000_01/mesh.obj
```
