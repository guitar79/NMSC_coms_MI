#cat all/2016/*2016*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/coms_mi_le1b_all_cf_2016.mkv

for i in 2011 2012
do
  echo "all/$i/*$i*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/coms_mi_le1b_all_cf_$i.mkv"
  all/$i/*$i*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/coms_mi_le1b_all_cf_$i.mkv
done
