# Repository Rename Guide: hanuman-chalisa → hanuman-gpt

## Overview

Comprehensive guide to rename the repository from "hanuman-chalisa" to "hanuman-gpt" to better reflect the AI-powered, multi-collection nature of the site.

## Benefits of Rename

- ✅ Aligns with new branding: "Hanuman GPT: AI Spiritual Guide"
- ✅ Reflects multi-collection support (not just Chalisa)
- ✅ Emphasizes AI/GPT features (guidance, search, RAG)
- ✅ More memorable and discoverable name

## Required Changes

### 1. GitHub Repository Settings

**On GitHub.com:**
1. Go to repository Settings
2. Under "General" → "Repository name"
3. Change from `hanuman-chalisa` to `hanuman-gpt`
4. Click "Rename"

**What GitHub does automatically:**
- ✅ Redirects old URL to new URL
- ✅ Updates all internal references
- ✅ Maintains all issues, PRs, commits, stars
- ✅ GitHub Pages URL changes

**New URLs after rename:**
- Repo: `https://github.com/YOUR_USERNAME/hanuman-gpt`
- Pages: `https://YOUR_USERNAME.github.io/hanuman-gpt/`

### 2. Update Local Repository

```bash
# Update remote URL
git remote set-url origin https://github.com/YOUR_USERNAME/hanuman-gpt.git

# Verify
git remote -v
```

### 3. Update _config.yml

```yaml
# Before
title: "Hanuman GPT: AI Spiritual Guide"
baseurl: "/hanuman-chalisa"
url: "https://YOUR_USERNAME.github.io"

# After
title: "Hanuman GPT: AI Spiritual Guide"
baseurl: "/hanuman-gpt"  # CHANGED
url: "https://YOUR_USERNAME.github.io"
```

### 4. Update Package References (if any)

Check these files for hardcoded repo references:
- `README.md` - Update GitHub URLs
- `package.json` (if exists) - Update repository field
- `CONTRIBUTING.md` (if exists) - Update clone URLs
- Documentation files in `docs/` - Update example URLs

```bash
# Find all mentions of old repo name
grep -r "hanuman-chalisa" --exclude-dir=_site --exclude-dir=.git .
```

### 5. Update Asset Paths (if absolute)

Check if any JavaScript, CSS, or templates use absolute paths:

```bash
# Check for hardcoded paths
grep -r "/hanuman-chalisa/" assets/ _layouts/ _includes/ --exclude-dir=_site
```

Most paths use `{{ '/path' | relative_url }}` which automatically updates with baseurl.

### 6. Update Environment Files

Check `.env` or `.env.example` for any repo-specific URLs:
```bash
# Example
SITE_URL=https://YOUR_USERNAME.github.io/hanuman-gpt
```

### 7. Update GitHub Actions (if any)

Check `.github/workflows/` for hardcoded repo references:
```yaml
# Update any hardcoded URLs in workflow files
```

### 8. Update Cloudflare Worker (if deployed)

The Cloudflare Worker URL for guidance API:
```javascript
// Update CORS allowed origins if using absolute URLs
const ALLOWED_ORIGINS = [
  'https://YOUR_USERNAME.github.io',
  'https://YOUR_USERNAME.github.io/hanuman-gpt'  // Updated
];
```

### 9. Custom Domain (if configured)

If using custom domain (e.g., hanumangpt.com):
- No changes needed - domain points to GitHub Pages regardless of repo name
- CNAME file remains the same

### 10. Analytics & Tracking

Update site references in:
- Google Analytics
- Google Search Console
- Social media metadata
- External documentation

## Step-by-Step Migration

### Phase 1: Preparation (5 min)

1. **Backup everything**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/hanuman-chalisa.git hanuman-chalisa-backup
   ```

2. **Document current state**:
   ```bash
   git log --oneline -5 > current-state.txt
   git remote -v >> current-state.txt
   ```

3. **Test local build**:
   ```bash
   bundle exec jekyll build
   bundle exec jekyll serve
   # Verify everything works
   ```

### Phase 2: Rename Repository (2 min)

1. Go to GitHub → Settings → General
2. Change repository name to `hanuman-gpt`
3. Click "Rename" and confirm

### Phase 3: Update Configuration (10 min)

1. **Update _config.yml**:
   ```bash
   # Change baseurl
   vim _config.yml
   # Change: baseurl: "/hanuman-gpt"
   ```

2. **Update local remote**:
   ```bash
   git remote set-url origin https://github.com/YOUR_USERNAME/hanuman-gpt.git
   ```

3. **Search and replace old references**:
   ```bash
   # Find all references
   grep -r "hanuman-chalisa" . --exclude-dir=_site --exclude-dir=.git | grep -v ".git/"

   # Replace in documentation
   find docs/ -type f -exec sed -i '' 's/hanuman-chalisa/hanuman-gpt/g' {} +

   # Update README
   sed -i '' 's/hanuman-chalisa/hanuman-gpt/g' README.md
   ```

4. **Test build**:
   ```bash
   bundle exec jekyll build
   # Check for warnings/errors
   ```

### Phase 4: Deploy & Verify (5 min)

1. **Commit changes**:
   ```bash
   git add -A
   git commit -m "Update baseurl and references for repo rename to hanuman-gpt"
   ```

2. **Push to new URL**:
   ```bash
   git push origin main
   ```

3. **Wait for GitHub Pages build** (1-2 minutes)

4. **Verify new URL**:
   ```
   https://YOUR_USERNAME.github.io/hanuman-gpt/
   ```

5. **Test old URL redirect**:
   ```
   https://YOUR_USERNAME.github.io/hanuman-chalisa/
   # Should redirect to /hanuman-gpt/
   ```

### Phase 5: Post-Migration Cleanup (10 min)

1. **Update external references**:
   - Social media bios
   - Portfolio websites
   - Blog posts linking to the project
   - README badges/shields

2. **Update analytics**:
   - Google Analytics property (if URL-based)
   - Google Search Console
   - Add new sitemap if needed

3. **Update documentation**:
   - CONTRIBUTING.md
   - Any external wikis
   - Presentation slides

4. **Notify users** (if public project):
   - Create release notes
   - Update project description
   - Pin issue announcing the change

## Potential Issues & Solutions

### Issue 1: Broken Links

**Symptom**: Images, CSS, or JS not loading

**Solution**: Check baseurl in _config.yml matches repo name:
```yaml
baseurl: "/hanuman-gpt"  # Must match repo name
```

### Issue 2: Old URLs Still Work

**Symptom**: Old URL `/hanuman-chalisa/` still shows old site

**Solution**:
- GitHub Pages cache takes time (up to 10 minutes)
- Clear browser cache
- Try incognito mode

### Issue 3: GitHub Pages 404

**Symptom**: New URL shows 404

**Solution**:
1. Check Settings → Pages is enabled
2. Verify branch is set to `main` (or `gh-pages`)
3. Rebuild: Make a dummy commit and push
4. Wait 2-3 minutes for build

### Issue 4: Assets Not Loading

**Symptom**: Page loads but no CSS/images

**Solution**: Check all asset paths use `relative_url`:
```liquid
❌ src="/hanuman-chalisa/images/..."
✅ src="{{ '/images/...' | relative_url }}"
```

### Issue 5: Cloudflare Worker CORS

**Symptom**: Guidance API fails with CORS error

**Solution**: Update Worker's allowed origins:
```javascript
const ALLOWED_ORIGINS = [
  'https://YOUR_USERNAME.github.io/hanuman-gpt'
];
```

## Verification Checklist

After migration, verify:

- [ ] New GitHub URL works: `github.com/YOUR_USERNAME/hanuman-gpt`
- [ ] New Pages URL works: `YOUR_USERNAME.github.io/hanuman-gpt/`
- [ ] Old GitHub URL redirects automatically
- [ ] Old Pages URL redirects (may take time)
- [ ] All pages load correctly (test 3-4 random pages)
- [ ] All images display correctly
- [ ] Theme switcher works
- [ ] Search functionality works
- [ ] Guidance/chat works
- [ ] Audio players work
- [ ] Navigation links work (prev/next)
- [ ] Book generator works
- [ ] Multi-collection navigation works
- [ ] Mobile responsive view works

## Rollback Plan

If anything goes wrong:

1. **Rename back on GitHub**:
   - Go to Settings → General
   - Rename back to `hanuman-chalisa`

2. **Revert local changes**:
   ```bash
   git reset --hard HEAD~1  # If you committed changes
   git remote set-url origin https://github.com/YOUR_USERNAME/hanuman-chalisa.git
   ```

3. **Restore _config.yml**:
   ```bash
   git checkout main -- _config.yml
   ```

## Timeline

**Total time: ~30 minutes**

- Preparation: 5 min
- GitHub rename: 2 min
- Update config: 10 min
- Deploy & verify: 5 min
- Post-migration: 10 min

## Recommended Timing

**Best time to rename:**
- During low-traffic hours
- Not immediately before a major release
- When you have time to monitor for issues

**Avoid renaming:**
- Right before a demo/presentation
- During peak usage hours
- When working on other major changes

## Post-Rename Benefits

After successful rename:
- ✅ Consistent branding across all touchpoints
- ✅ Better SEO (name matches site title)
- ✅ More discoverable GitHub repo
- ✅ Clearer project purpose
- ✅ Sets up for future expansion (more texts, more AI features)

## Notes

- GitHub automatically redirects old URLs indefinitely
- All git history, stars, forks, issues preserved
- No data loss
- Collaborators automatically redirected
- External links gradually update via redirects
- Search engines re-index over time (submit new sitemap)

## Support

If issues arise:
1. Check GitHub Pages build log
2. Test locally first: `bundle exec jekyll serve`
3. Verify baseurl matches repo name exactly
4. Check browser console for asset 404s
5. Clear all caches (browser, CDN, GitHub)
