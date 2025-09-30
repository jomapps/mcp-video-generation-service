# MCP Video Generation Service - Deployment Guide

## 🚀 Quick Deploy

### Step 1: Get FAL.ai API Key
1. Go to https://fal.ai
2. Sign up / Log in
3. Get API key from dashboard

### Step 2: Create .env File
```bash
cd /var/www/movie-generation-platform/services/mcp-video-generation-service

# Copy template
cp .env.prod.example .env

# Edit and add your FAL.ai API key
nano .env
```

Update this line:
```env
FAL_API_KEY=your-actual-fal-key-here
```

### Step 3: Install & Deploy
```bash
# Install dependencies
pip3 install -r requirements.txt

# Deploy with PM2
pm2 start "python3 -m src.mcp_server" \
  --name mcp-video-generation-service \
  --cwd /var/www/movie-generation-platform/services/mcp-video-generation-service

# Save
pm2 save

# Verify
pm2 list | grep video-generation
pm2 logs mcp-video-generation-service --lines 10
```

## ✅ Configuration

### Already Configured (No Changes Needed)
- OpenRouter API Key: ✅
- OpenRouter Model: anthropic/claude-sonnet-4.5 ✅
- PayloadCMS URL: https://auto-movie.ft.tc ✅
- Brain Service URL: https://brain.ft.tc ✅

### You Need To Add
- ⚠️ FAL.ai API Key (REQUIRED)
- PayloadCMS API Key (optional)

## 🎯 What This Service Does

Converts storyboard frames into video segments using FAL.ai:
- Input: Generated images + storyboard metadata
- Output: Video segments (MP4 files)
- Provider: FAL.ai (veo3/fast/image-to-video)

## 📊 Next Steps

After deploying this service:
1. Deploy **Video Editor Service** (concatenates segments)
2. Deploy **Final QC Service** (quality checks)
3. Deploy **Distribution Service** (final export)

---

**Service Path**: `/var/www/movie-generation-platform/services/mcp-video-generation-service`
