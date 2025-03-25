def generate_html(articles):
    html_output = ""
    for article in articles:
        html_output += f'''
<li>
    <span>
        <a href="{article['link']}">
            <img src="{article['img_src']}" alt="{article['alt_text']}"/>
        </a>
    </span>
    <a href="{article['link']}">{article['title']}</a>
</li>
'''
    return html_output

articles = [
    {
        "title": "[Brief Guide] How to Install macOS on a Non-Apple PC",
        "link": "../mac-tips/how-to-install-macos-on-a-non-apple-pc.html",
        "img_src": "../images/mac-tips/how-to-install-macos-on-a-non-apple-pc/how-to-install-macos-on-pc.webp",
        "alt_text": "install macOS on a non-apple PC"
    },
    {
        "title": "How to Install a Windows 11/Mac Dual Boot System on Mac [All Processor]",
        "link": "../mac-tips/how-to-install-a-windows-mac-dual-boot-system-on-mac.html",
        "img_src": "../images/mac-tips/how-to-install-a-windows-mac-dual-boot-system-on-mac/how-to-install-a-dual-system-on-mac.webp",
        "alt_text": "How to install a dual system on mac"
    },
    {
        "title": "[3 Ways in Detail] How to Migrate Data from an Old Mac to a New Macbook Pro",
        "link": "../mac-tips/how-to-migrate-data-from-an-old-mac-to-a-new-macbook-pro.html",
        "img_src": "../images/mac-tips/how-to-migrate-data-from-an-old-mac-to-a-new-macbook-pro/how-to-migrate-data-from-an-old-mac-to-a-new-macbook-pro.webp",
        "alt_text": "Migrate Data on mac"
    },
    {
        "title": "Discover What's New in macOS Sequoia: Enhanced Features and Improvements",
        "link": "../mac-tips/what-is-new-in-macos-sequoia.html",
        "img_src": "../images/mac-tips/what-is-new-in-macos-sequoia/what-is-new-in-macos-sequoia.webp",
        "alt_text": "What is new in macOS Sequoia"
    },
    {
        "title": "[Full Guide] How to Check Your Macbook Pro's macOS Information and Battery Status",
        "link": "../mac-tips/how-to-check-your-macbook-pro-system-information-and-battery-status.html",
        "img_src": "../images/mac-tips/how-to-check-your-macbook-pro-system-information-and-battery-status/how-to-check-your-macbook-pro-system-information-and-battery-status.webp",
        "alt_text": "How To Check Your Macbook Pro System Information And Battery Status"
    },
    {
        "title": "How to Reset MacBook Pro to Factory Settings without Password",
        "link": "../mac-tips/how-to-factory-reset-macbook-pro.html",
        "img_src": "../images/mac-tips/how-to-factory-reset-macbook-pro/recovery-mode-reinstall-macos.png",
        "alt_text": "How to Reset MacBook Pro to Factory Settings without Password"
    },
    {
        "title": "Boost Productivity: 16 Efficiency Tips for Using the Touch Bar on Your MacBook Pro",
        "link": "../mac-tips/16-tips-for-using-touchbar-on-macbook-pro.html",
        "img_src": "../images/mac-tips/16-tips-for-using-touchbar-on-macbook-pro/make-good-use-of-your-touch-bar.webp",
        "alt_text": "Boost Productivity: 16 Efficiency Tips for Using the Touch Bar on Your MacBook Pro"
    },
    {
        "title": "[7 Solutions] How to Fix a Mac That Won't Start Up",
        "link": "../mac-tips/16-tips-for-using-touchbar-on-macbook-pro.html",
        "img_src": "../images/mac-tips/how-to-fix-mac-will-not-start-up/how-to-fix-mac-will-not-start-up.webp",
        "alt_text": "[7 Solutions] How to Fix a Mac That Won't Start Up"
    },
    {
        "title": "Could the Apple Vision Pro Replace the MacBook Pro? Here’s What We Found…",
        "link": "../mac-tips/could-the-apple-vision-pro-repalce-the-macbook-pro.html",
        "img_src": "../images/mac-tips/could-the-apple-vision-pro-repalce-the-macbook-pro/could-the-vision-pro-replace-the-mac.webp",
        "alt_text": "Could the Apple Vision Pro Replace the MacBook Pro? Here’s What We Found…"
    },
    {
        "title": "How to Install or Use Linux on a Mac: A Comprehensive Guide",
        "link": "../mac-tips/how-to-install-or-use-linux-on-mac.html",
        "img_src": "../images/mac-tips/how-to-install-or-use-linux-on-mac/how-to-install-or-use-linux-on-mac.webp",
        "alt_text": "How to Install or Use Linux on a Mac: A Comprehensive Guide"
    },
    {
        "title": "10 Ways to Free up Space on Mac",
        "link": "../mac-tips/how-to-free-up-space-on-mac.html",
        "img_src": "../images/mac-tips/how-to-free-up-space-on-mac/manage-mac-storage.png",
        "alt_text": "10 Ways to Free up Space on Mac"
    },
    {
        "title": "Configuring a Windows Keyboard for Mac or Vice Versa",
        "link": "../mac-tips/configuring-a-windows-keyboard-for-mac-or-vice-versa.html",
        "img_src": "../images/mac-tips/configuring-a-windows-keyboard-for-mac-or-vice-versa/use-mac-keyboard-on-windows-or-reverse.webp",
        "alt_text": "Configuring a Windows Keyboard for Mac or Vice Versa"
    },
    
    
    

    
    # 可以在这里添加更多文章信息
]

html_code = generate_html(articles)
print(html_code)
