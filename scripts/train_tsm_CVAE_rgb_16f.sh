python3 "/content/drive/My Drive/samsung/main.py" CVAE RGB \
     --arch mobilenetv2 --num_segments 16 \
     --gd 20 --lr 0.001 --wd 1e-4 --lr_steps 20 40 --epochs 50 \
     --batch-size 4 -j 16 --dropout 0.5 --consensus_type=avg --eval-freq=1 \
     --shift --shift_div=8 --shift_place=blockres --npb

     
