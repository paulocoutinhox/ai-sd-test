import torch
from diffusers import StableDiffusionImg2ImgPipeline
from diffusers.utils import load_image

# ref
# https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/img2img

# image
img_url = "extras/images/model.jpg"
image = load_image(img_url)

# model
sd_model_path = "Lykon/dreamshaper-8"

pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    sd_model_path,
    use_safetensors=True,
    # torch_dtype=torch.float16,
)

# torch
torch_device = (
    torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
)

# pipe
pipe = pipe.to(torch_device)

# prompt
prompt = "a man face with red hair"
negative_prompt = "tattooing, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, braid hair"

# generate
output = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    image=image,
    num_inference_steps=20,
    strength=0.75,
    guidance_scale=7.5,
)

# save image
out_image = output.images[0]
out_image.save("output-img2img.png")
