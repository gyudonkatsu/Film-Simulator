import streamlit as st
from PIL import Image, ImageEnhance, ImageOps

logo = Image.open("assets/Logo.png")

# 필터 함수 3개 간단히 구현
def kodak_style(image):
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(1.5)
    image = ImageOps.autocontrast(image)
    return image

def fuji_style(image):
    image = image.convert("L").convert("RGB")  # 흑백 후 컬러 톤
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(1.2)

def hk_style(image):
    r, g, b = image.split()
    r = r.point(lambda i: i * 1.1)
    b = b.point(lambda i: i * 1.2)
    return Image.merge("RGB", (r, g, b))

def apply_filter(image, filter_name):
    if filter_name == "Kodak":
        return kodak_style(image)
    elif filter_name == "Fuji":
        return fuji_style(image)
    elif filter_name == "Hong Kong 2046":
        return hk_style(image)
    else:
        return image

# Streamlit UI 시작
st.title("🎞️ Film Simulator Simple App")

uploaded_file = st.file_uploader("사진 업로드 (jpg, png)", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="원본 이미지", use_column_width=True)

    filter_name = st.selectbox("필터 선택", ["Kodak", "Fuji", "Hong Kong 2046"])

    if st.button("필터 적용"):
        filtered_img = apply_filter(image, filter_name)
        st.image(filtered_img, caption=f"{filter_name} 필터 적용 결과", use_column_width=True)

        # 다운로드 버튼
        import io
        buf = io.BytesIO()
        filtered_img.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="다운로드",
            data=byte_im,
            file_name=f"{filter_name.lower().replace(' ', '_')}.jpg",
            mime="image/jpeg"
        )
