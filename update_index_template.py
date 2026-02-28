import re

with open('f:/code/web/MMC/frontend/templates/index.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace banner buttons
template = template.replace('href="https://mulumesfincharity.org/causes/"', 'href="{% url \'web:programs\' %}"')
template = template.replace('href="https://mulumesfincharity.org/contact-us/"', 'href="{% url \'web:contact\' %}"')

# Brands Carousel
brands_carousel_pattern = re.compile(
    r'<div class="elementor-image-carousel swiper-wrapper" aria-live="off">.*?</div>\s*</div>',
    re.DOTALL
)

brands_carousel_replacement = """<div class="elementor-image-carousel swiper-wrapper" aria-live="off">
                                {% for partner in partners %}
                                <div class="swiper-slide" role="group">
                                    <figure class="swiper-slide-inner">
                                        {% if partner.logo %}
                                        <img decoding="async" class="swiper-slide-image" src="{{ partner.logo.url }}" alt="{{ partner.name }}">
                                        {% else %}
                                        <img decoding="async" class="swiper-slide-image" src="{% static 'images/brand-01.png' %}" alt="{{ partner.name }}">
                                        {% endif %}
                                    </figure>
                                </div>
                                {% empty %}
                                <div class="swiper-slide" role="group"><figure class="swiper-slide-inner"><img decoding="async" class="swiper-slide-image" src="{% static 'images/brand-01.png' %}" alt="brand-01"></figure></div>
                                <div class="swiper-slide" role="group"><figure class="swiper-slide-inner"><img decoding="async" class="swiper-slide-image" src="{% static 'images/brand-02.png' %}" alt="brand-02"></figure></div>
                                {% endfor %}
                            </div>
                        </div>"""

template = brands_carousel_pattern.sub(brands_carousel_replacement, template)


# Programs/Causes Difference Slider
programs_carousel_pattern = re.compile(
    r'<div class="difference__slider swiper">.*?<div class="slider-navigation difference-slider-navigation',
    re.DOTALL
)

programs_carousel_replacement = """<div class="difference__slider swiper">
					<div class="swiper-wrapper">
						{% for program in programs %}
						<div class="swiper-slide">
							<div class="difference__single-wrapper">
							<div class="difference__single difference__single-first" {% if program.image %}style="background-image:url('{{ program.image.url }}');"{% else %}style="background-image:url('{% static 'images/cat_bg-one-1.png' %}');"{% endif %}>
								<div class="difference__single-thumb">
									<i class="icon-education"></i>
								</div>
								<div class="difference__single-content">
									<h5><a href="{% url 'web:program_detail' program.slug %}">{{ program.title }}</a></h5>
									<p>{{ program.description|truncatewords:15 }}</p>
								</div>
							</div>
							</div>
						</div>
						{% empty %}
						<!-- Fallback static content if no programs -->
						<div class="swiper-slide">
							<div class="difference__single-wrapper">
							<div class="difference__single difference__single-first" style="background-image:url('{% static 'images/cat_bg-one-1.png' %}');">
								<div class="difference__single-thumb">
									<i class=" icon-education"></i>
								</div>
								<div class="difference__single-content">
									<h5><a href="{% url 'web:programs' %}">Education Support</a></h5>
									<p>Providing exercise books and learning materials to displaced students affected by conflict in Tigray.</p>
								</div>
							</div>
							</div>
						</div>
						{% endfor %}
					</div>
				</div>
                <div class="slider-navigation difference-slider-navigation"""

template = programs_carousel_pattern.sub(programs_carousel_replacement, template)

# Latest News
latest_news_pattern = re.compile(
    r'<div class="row gutter-24 mt-4">.*?<div class="elementor-element elementor-element-bbfb9c9',
    re.DOTALL
)

latest_news_replacement = """<div class="row gutter-24 mt-4">
                {% for post in latest_posts %}
                <div class="col-12 col-lg-4">
                    <div class="blog__single-wrapper pb-3">
                        <div class="blog__single van-tilt">
                            <div class="blog__single-thumb">
                                <a href="{% url 'web:blog_detail' post.slug %}">
                                    {% if post.image %}
                                    <img decoding="async" src="{{ post.image.url }}" alt="{{ post.title }}">
                                    {% else %}
                                    <img decoding="async" src="{% static 'images/five-7.png' %}" alt="{{ post.title }}">
                                    {% endif %}
                                </a>
                                <div class="tag">
                                    <a href="javascript:void(0)"><i class="fa-solid fa-tags"></i> {{ post.category.name|default:"News" }}</a>
                                </div>
                            </div>
                            <div class="blog__single-inner">
                                <div class="blog__single-meta">
                                    <p><i class="icon-user"></i>{{ post.author }}</p>
                                    <p><i class="icon-calendar"></i>{{ post.published_date|date:"d M Y" }}</p>
                                </div>
                                <div class="blog__single-content">
                                    <h5><a href="{% url 'web:blog_detail' post.slug %}">{{ post.title }}</a></h5>
                                </div>
                                <div class="blog__single-cta">
                                    <a href="{% url 'web:blog_detail' post.slug %}" aria-label="blog details" title="blog details">Read More<i class="fa-solid fa-circle-arrow-right"></i></a>
                                </div>
                            </div>
                            <img decoding="async" class="spade-two" src="{% static 'images/spade.png' %}" alt="">
                        </div>
                    </div>
                </div>
                {% empty %}
                <p>No posts available.</p>
                {% endfor %}
            </div>
        </div>
        <div class="elementor-element elementor-element-bbfb9c9"""

template = latest_news_pattern.sub(latest_news_replacement, template)

# Fix double static paths like src="{% static '{% static 'images/foo.png' %}' %}"
# Since some images were already matched with static in the previous step
template = re.sub(r'{%\s*static\s*\'(.*?)\'\s*%}', lambda m: f'{{% static \'{m.group(1).replace("{% static \\\'", "").replace("\\\' %}", "")}\' %}}', template)

with open('f:/code/web/MMC/frontend/templates/index.html', 'w', encoding='utf-8') as out:
    out.write(template)
print('Template dynamic blocks added')
