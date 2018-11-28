#cat 07/*.png | ffmpeg -framerate 10 -f image2pipe -i - coms_mi_le1b_com_a_201607_fr10.mkv
#cat 2016/coms_mi_le1b_ir1_a_201601*.png | ffmpeg -framerate 5 -f image2pipe -i - coms_mi_le1b_ir1_a_201601_fr10.mkv
#cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/wv/2017/*2017*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/wv/coms_mi_le1b_wv_cf_2017.mkv
#cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/swir/2017/*2017*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/swir/coms_mi_le1b_swir_cf_2017.mkv
#cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/vis/2017/*2017*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/vis/coms_mi_le1b_vis_cf_2017.mkv
#cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/com/2017/*2017*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/com/coms_mi_le1b_com_cf_2017.mkv
#2010
cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/vis/2010/*2010*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/vis/coms_mi_le1b_vis_cf_2010.mkv
cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/ir1/2010/*2010*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/ir1/coms_mi_le1b_ir1_cf_2010.mkv
cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/ir2/2010/*2010*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/ir2/coms_mi_le1b_ir2_cf_2010.mkv
cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/wv/2010/*2010*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/wv/coms_mi_le1b_wv_cf_2010.mkv
cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/swir/2010/*2010*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/swir/coms_mi_le1b_swir_cf_2010.mkv
cat /run/user/1000/gvfs/smb-share:server=parksrne,share=coms_mi/le1b/cf/com/2010/*2010*.png | ffmpeg -framerate 5 -f image2pipe -i - mkv/com/coms_mi_le1b_com_cf_2010.mkv


