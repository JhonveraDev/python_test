import imageio
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('imagen_pri.gif', images)