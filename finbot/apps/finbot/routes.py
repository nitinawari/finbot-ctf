"""Route handlers for the OWASP FinBot CTF platform pages"""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse

from finbot.core.templates import TemplateResponse

finbot_templates = TemplateResponse("finbot/apps/finbot/templates")
web_templates = TemplateResponse("finbot/apps/web/templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """OWASP FinBot CTF home page"""
    return finbot_templates(request, "home.html")


@router.get("/portals", response_class=HTMLResponse)
async def portals(request: Request):
    """Portals page - access vendor, admin, and CTF portals"""
    return finbot_templates(request, "portals.html")


@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About OWASP FinBot - project info, team, and contributors"""
    return web_templates(request, "pages/finbot.html")


# Error page test routes (for development/testing)
@router.get("/test/404")
async def test_404():
    """Test 404 error page"""
    raise HTTPException(status_code=404, detail="Test 404 error")


@router.get("/test/403")
async def test_403():
    """Test 403 error page"""
    raise HTTPException(status_code=403, detail="Test 403 error")


@router.get("/test/400")
async def test_400():
    """Test 400 error page"""
    raise HTTPException(status_code=400, detail="Test 400 error")


@router.get("/test/500")
async def test_500():
    """Test 500 error page"""
    raise HTTPException(status_code=500, detail="Test 500 error")


@router.get("/test/503")
async def test_503():
    """Test 503 error page"""
    raise HTTPException(status_code=503, detail="Test 503 error")


@router.get("/api/test/404")
async def api_test_404():
    """Test 404 API error response"""
    raise HTTPException(status_code=404, detail="API endpoint not found")


@router.get("/api/test/500")
async def api_test_500():
    """Test 500 API error response"""
    raise HTTPException(status_code=500, detail="Internal API error")
