document.addEventListener('DOMContentLoaded', (event) => {
    const works = [
        {
            title: 'Anime-x-Quiz website project',
            content: `<div class="work-github">
                        <a href="https://github.com/HichamLuffy/website-project" target="_blank">
                            <img src="https://github-readme-stats.vercel.app/api/pin/?username=HichamLuffy&repo=website-project&theme=dark" alt="Readme Card">
                        </a>
                        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7180740100534730752" width="560" height="315" frameborder="0" allowfullscreen=""></iframe>
                      </div>`
        },
        {
            title: 'Thumbnails',
            content: `<div class="work-thumbnails">
                        <img src="/statics/images/mywork/thumbnail1.jpg" alt="Thumbnail 1">
                        <img src="/statics/images/mywork/thumbnail2.webp" alt="Thumbnail 2">
                        <img src="/statics/images/mywork/thumbnail3.webp" alt="Thumbnail 3">
                        <img src="/statics/images/mywork/thumbnail4.webp" alt="Thumbnail 4">
                        <img src="/statics/images/mywork/thumbnail5.webp" alt="Thumbnail 5">
                        <img src="/statics/images/mywork/thumbnail6.webp" alt="Thumbnail 6">
                        <img src="/statics/images/mywork/thumbnail7.webp" alt="Thumbnail 7">
                        <img src="/statics/images/mywork/thumbnail8.webp" alt="Thumbnail 8">
                        <img src="/statics/images/mywork/thumbnail9.jpg" alt="Thumbnail 9">
                      </div>`
        },
        {
            title: 'UI Design Websites',
            content: `<div class="work-ui-design">
                        <img src="/statics/images/mywork/finaldesign.png" alt="UI Design">
                      </div>`
        },
        {
            title: 'Edited Videos',
            content: `<div class="work-videos">
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/NKZ6r-ylqZc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/Um9-CIYJlmg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        </div>`
        },
        {
            title: 'Blender Projects',
            content: `<div class="work-thumbnails">
                        <a href="/statics/images/mywork/blender1.png" target="_blank"><img src="/statics/images/mywork/blender1.png" alt="blender 1"></a>
                        <a href="/statics/images/mywork/blender2.png" target="_blank"><img src="/statics/images/mywork/blender2.png" alt="blender 2"></a>
                        <a href="/statics/images/mywork/blender5.png" target="_blank"><img src="/statics/images/mywork/blender5.png" alt="blender 5"></a>
                        <a href="/statics/images/mywork/blender3.png" target="_blank"><img src="/statics/images/mywork/blender3.png" alt="blender 3"></a>
                        <a href="/statics/images/mywork/blender4.png" target="_blank"><img src="/statics/images/mywork/blender4.png" alt="blender 4"></a>
                        <a href="/statics/images/mywork/blender6.png" target="_blank"><img src="/statics/images/mywork/blender6.png" alt="blender 6"></a>
                        <video width="560" height="315" controls>
                            <source src="https://cdn.discordapp.com/attachments/1084295186542235751/1103350229450903633/sadd.mp4?ex=66292c79&is=6616b779&hm=073f2c3a3959822b1499ea17400ee66502a14af2368e8cf6139dd260efd55d38&" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>
                        <iframe width="560" height="315" src="https://www.youtube.com/embed/pe5t-SgFBZE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        </div>`
        }
    ];

    const workContainer = document.querySelector('.work-container');

    works.forEach(work => {
        const workItem = document.createElement('div');
        workItem.classList.add('work-item');
        workItem.innerHTML = `
            <h3 class="work-title">${work.title}</h3>
            <div class="work-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">${work.content}</div>
        `;
        workContainer.appendChild(workItem);
    });

    // Event delegation to handle clicks on work titles
    workContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('work-title')) {
            const content = e.target.nextElementSibling;
            content.style.maxHeight = content.style.maxHeight === '0px' ? `${content.scrollHeight}px` : '0px';
        }
    });

    const timeline = document.querySelector('.timeline');

    timeline.addEventListener('click', function(e) {
        const timelineItem = e.target.closest('.timeline-item');
        if (timelineItem) {
            const id = timelineItem.getAttribute('data-id');
            const content = document.getElementById(`${id}-details`);
            const isOpen = content.style.maxHeight !== '';
            content.style.maxHeight = isOpen ? '' : `${content.scrollHeight}px`;
        }
    });

    const sections = document.querySelectorAll("section[id]");

  // Add an event listener listening for scroll
    window.addEventListener("scroll", function() {
    // Variable to keep track of the current section
    let currentSection = "";

    // Check the scroll position against each section's top and bottom
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionBottom = sectionTop + section.clientHeight;
      if (pageYOffset >= sectionTop - 50 && pageYOffset <= sectionBottom - 50) {
        // This is the current section
        currentSection = section.id;
      }
    });

    // Remove the 'active' class from all the nav links
    // Then add 'active' class to the nav link that corresponds to the current section
    document.querySelectorAll('.navbar a').forEach(a => {
      a.classList.remove('active');
      if (a.getAttribute('href').includes(currentSection)) {
        a.classList.add('active');
      }
    });
  });
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('showscroll');
        } else {
            entry.target.classList.remove('showscroll');
        }
    });
    });

    const hiddenElements = document.querySelectorAll('.scrollefeect');
    const hiddenElementsbox = document.querySelectorAll('.scrollefeectbox');
    hiddenElements.forEach((element) => {
        observer.observe(element);
    });
    hiddenElementsbox.forEach((element) => {
        observer.observe(element);
    });

});