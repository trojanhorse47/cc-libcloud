from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# User email
USER_ID = 'pippo-530@mylibcloud.iam.gserviceaccount.com'

# Path to JSON credential file
GCP_CREDENTIALS_JSON = 'E:\Download\mylibcloud-df9a6978df89.json'

# Project ID
GCP_PROJECT_ID = 'mylibcloud'

# Zone name to where create he new VM
GCP_ZONE = 'us-central1-a'

# Machine name
MACHINE_NAME = 'mymachine'

try:
    # Get GCP driver
    print("Getting GCP driver...")
    ComputeEngine = get_driver(Provider.GCE)
    driver = ComputeEngine(USER_ID, GCP_CREDENTIALS_JSON, project=GCP_PROJECT_ID, datacenter=GCP_ZONE)

    # Get image
    print("Fetching image list...")
    images = driver.list_images()
    for (i, image) in enumerate(images):
        print(f"{i + 1:>3}) {image.name}")
    image_num = int(input("\nSelect image: ")) - 1
    image = driver.ex_get_image(images[image_num].name)

    # Get machine size
    print("Fetching machine size list...")
    sizes = driver.list_sizes()
    for (i, size) in enumerate(sizes):
        print(f"{i + 1:>3}) {size.name}")
    size_num = int(input("\nSelect size: ")) - 1
    size = driver.ex_get_size(sizes[size_num].name)

    # Create VM
    print("Creating VM...")
    node = driver.create_node(name=MACHINE_NAME, image=image, size=size)

    print(f'VM {MACHINE_NAME} succesfully created! ID: {node.id}')
    
except Exception as e:
    print(f"Error: {e}")
