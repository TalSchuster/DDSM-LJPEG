#!/usr/bin/env bash

ljpeg2raw=/home/xmchiu/Mammo_Challenge/DDSM/DDSM-LJPEG/decompress_ljpeg.py
path=/home/xmchiu/Mammo_Challenge/DDSM/test_images/test_case
echo "path is $path"

cd $path

for sub_path in $(ls)
do
	cd $sub_path
	cur_path=$(pwd)
	echo "Current path is $cur_path"

	# run python script
	# to convert .LJPEG to raw image
	raw2pnm_command_split=$(python $ljpeg2raw --dir $cur_path)
	# echo $raw2pnm_command

	# convert raw image to .pnm format
	i=0
	for item in $raw2pnm_command_split
	do
		let "i=$i+1"

		# check whether the new command begins
		let "v=$i%5"
		first_flag=$[$v==1]
		# echo $i
		echo $item

		# check whether a full command ends
		let "u=$i%5"
		round_flag=$[$u==0]
		if [$first_flag == '1'];then
			raw2pnm_command=$item
		else
			raw2pnm_command=$raw2pnm_command" "$item
		fi

		if [$round_flag == '1'];then
			echo $raw2pnm_command
		fi

	done

	cd ..
done

