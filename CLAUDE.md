# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Turrant.ai marketing website - a single-page landing page for an AI-powered document collection platform that works via WhatsApp.

## Development Commands

```bash
# Start local development server on port 3000
npm start
```

## Architecture

This is a static single-page website with no build step:

- **index.html** - The entire landing page (HTML, Tailwind CSS, and vanilla JavaScript inline)
- **package.json** - Only contains a serve script for local development
- **railway.json** - Railway deployment configuration

### Technology Stack

- **Tailwind CSS** - Loaded via CDN with custom configuration inline
- **Lucide Icons** - Icon library loaded via unpkg CDN
- **Google Fonts** - Plus Jakarta Sans font family

### Key Inline Components

All JavaScript is embedded in the HTML file:
- Industry tab switching (`showIndustry()` function around line 637)
- FAQ accordion toggle (`toggleFaq()` function around line 954)
- Mobile menu toggle (inline onclick handler)

### Tailwind Configuration

Custom Tailwind config is defined inline in a `<script>` tag:
- Custom font family: Plus Jakarta Sans
- Brand colors: `brand-red` (#dc2626), `brand-green` (#059669)

### Custom CSS Classes

Defined in the `<style>` block:
- `.text-gradient` - Emerald gradient text effect
- `.glass` - Frosted glass backdrop effect
- `.whatsapp-bg` - WhatsApp chat background pattern
- `.hero-gradient` - Hero section radial gradient
- `.animate-float` - Floating animation keyframes

## Deployment

Deployed to Railway using nixpacks. The `npm start` command serves the static files using the `serve` package on port 3000.
