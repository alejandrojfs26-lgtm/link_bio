import reflex as rx


def chat_loader() -> rx.Component:
    return rx.html(
        """
        <div class="chat-loader">
            <div class="box"></div>
            <svg viewBox="0 0 100 100" width="100" height="100">
                <clipPath id="clip-uiverse">
                    <polygon points="50,10 60,40 90,40 65,60 75,90 50,70 25,90 35,60 10,40 40,40" />
                    <polygon points="50,10 60,40 90,40 65,60 75,90 50,70 25,90 35,60 10,40 40,40" />
                    <polygon points="50,10 60,40 90,40 65,60 75,90 50,70 25,90 35,60 10,40 40,40" />
                    <polygon points="50,10 60,40 90,40 65,60 75,90 50,70 25,90 35,60 10,40 40,40" />
                    <polygon points="50,10 60,40 90,40 65,60 75,90 50,70 25,90 35,60 10,40 40,40" />
                    <polygon points="50,10 60,40 90,40 65,60 75,90 50,70 25,90 35,60 10,40 40,40" />
                    <polygon points="50,10 60,40 90,40 65,60 75,90 50,70 25,90 35,60 10,40 40,40" />
                </clipPath>
            </svg>
        </div>
        """
    )
