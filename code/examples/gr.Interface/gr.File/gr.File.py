# 导入所需的库
import os  # 用于文件操作
import gradio as gr  # 导入Gradio库用于创建Web界面


def process_file(image_file, pdf_file):
    """
    处理上传的图片和PDF文件
    Args:
        image_file: 上传的图片文件对象
        pdf_file: 上传的PDF文件对象
    Returns:
        str: 返回处理结果信息
    """
    
    # 检查是否上传了图片文件
    if image_file is None:
        return "Please upload an image"
    # 检查是否上传了PDF文件
    elif pdf_file is None:
        return "Please upload a pdf"
    else:
        # 获取文件名
        image_file_name = image_file.name
        pdf_file_name = pdf_file.name
        # 返回文件名信息
        return f"上传的图片路径: {image_file_name}\n 上传的PDF路径: {pdf_file_name}"


if __name__ == "__main__":
    # 创建Gradio界面
    iface = gr.Interface(
        # 指定处理函数
        fn=process_file,
        # 定义输入组件：两个文件上传框
        inputs=[
            gr.File(label="Upload  images", file_types=["image"]),  # 图片上传组件，限制只能上传图片
            gr.File(label="Upload an pdf", file_types=[".pdf"])     # PDF上传组件，限制只能上传PDF
        ],
        # 定义输出组件：文本框
        outputs=gr.Textbox(label="Output"),
        # 设置界面标题
        title="File Upload",
        # 设置界面描述
        description="Upload an image or pdf",
    )

    # 启动Gradio应用
    iface.launch()

    