import re
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]


def read_in_txt_annotations(file_name):
	file = open(file_name)
	
	lines = file.readlines()

	for line in lines:

		i = str(line).replace("2007_000027.jpg_","")

		parts = i.partition(',')
 		
		if (parts[2] in "1 0\n"): 
			print("got no {}".format(parts[0]))

		else:
			strings = parts[2].split(" ")

			#print("we got {} at {}".format(parts[0],parts[2]))
		

			nums = [] 

			for item in strings:

				if len(item) is not 1:

					nums.append(int(re.sub("[\s+]", "", item)))
					#(re.sub("[\D]", "", item))

			y_1 = nums[0] // 400

			y_2 = nums[len(nums) - 2] // 400

			x_1 = nums[0] % 400

			x_2 = x_1 + nums[1]

			print("x_1 {} x_2 {} y_1 {} y_2 {} ".format(x_1, x_2, y_1, y_2))




read_in_txt_annotations("/Users/yawensun/Desktop/NCData/train/2007_000027.txt")



