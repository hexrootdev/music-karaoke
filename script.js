const p = document.querySelectorAll("p")
const player = document.querySelector("#player")
const volume_bar = document.querySelector("#volume-bar")
const progress_bar = document.querySelector("#progress-bar")

player.volume = 0.1
volume_bar.value = 10
volume_bar.addEventListener("input", () => {player.volume = volume_bar.value / 100})
player.addEventListener("loadedmetadata", () => {progress_bar.max = player.duration})

p.forEach(line => {
    line.addEventListener('click', () => {
        const active = document.querySelector(".active")

        if (active) {
            active.classList.remove("active")
        }

        line.classList.add("active")
        progress_bar.value  = line.dataset.time

        player.play()
        play_icon.src = "icons/pause-icon.svg"

        line.scrollIntoView({behavior: "smooth", block: "center"})
    })
})

player.addEventListener('timeupdate', () => {
    progress_bar.value = player.currentTime
    let curLine = null
    p.forEach(line => {
        if (player.currentTime >= Number(line.dataset.time)) {
            curLine = line
        }
    })
    if (curLine && !curLine.classList.contains("active")) {
        const active = document.querySelector("p.active")
        if (active) { active.classList.remove("active") }
        curLine.classList.add("active")
        curLine.scrollIntoView({behavior: "smooth", block: "center"})
    }
    
})

progress_bar.addEventListener("input", () => {player.currentTime = progress_bar.value})


const play_btn = document.querySelector("#play-btn")
const play_icon = play_btn.querySelector("img")

play_btn.addEventListener("click", () => {
    if (player.paused) {
        player.play()
        play_icon.src = "icons/pause-icon.svg"
    }
    else {
        player.pause()
        play_icon.src = "icons/play-icon.svg"
    }
})

player.addEventListener("ended", () => {
    play_icon.src = "icons/play-icon.svg"
})


// --- громкость
const volume_btn = document.querySelector("#volume-btn")
const volume_box = document.querySelector("#volume-box")

volume_btn.addEventListener("click", () => {volume_box.classList.toggle("is-open")})






