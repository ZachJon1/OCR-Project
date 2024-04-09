import matplotlib.pyplot as plt


def plotImage(image, title='Image'):
    plt.figure(figsize=(10, 10))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.savefig("./plots/preProcessed.jpg")
    plt.show()
    
   