INPUT_IMAGE=../experiments/lr/TEST_4K_0005655.png
IN_CROP_DIR=../experiments/crop_lr
OUT_CROP_DIR=../results/SPSR/set5

python get_crops.py $INPUT_IMAGE $IN_CROP_DIR

python test.py -opt options/test/test_spsr.json

python stitch_crops.py $OUT_CROP_DIR $INPUT_IMAGE
