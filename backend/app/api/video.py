from fastapi import APIRouter
from loguru import logger
from app.services.video import generate_video
from app.schemas.video import VideoGenerateRequest, VideoGenerateResponse

router = APIRouter()


@router.post("/generate")
async def generate_video_endpoint(request: VideoGenerateRequest):
    """生成视频"""
    try:
        video_file = await generate_video(request)
        # 转换为相对路径
        video_url = (
            "http://ai-story-server.sineai.cn/tasks/" + video_file.split("/tasks/")[-1]
        )
        return VideoGenerateResponse(success=True, data={"video_url": video_url})
    except Exception as e:
        logger.error(f"Failed to generate video: {str(e)}")
        return VideoGenerateResponse(success=False, message=str(e))
