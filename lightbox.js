/* Click a gallery photo to enlarge it. */
(() => {
	var box = document.getElementById("lightbox");
	if (!box || typeof box.showModal !== "function") return;

	var img = box.querySelector("img");
	var caption = box.querySelector(".lightbox-caption");
	var closeBtn = box.querySelector(".lightbox-close");

	document.querySelectorAll(".shot").forEach((shot) => {
		shot.addEventListener("click", () => {
			img.src = shot.dataset.full;
			img.alt = shot.querySelector("img").alt;
			caption.textContent = shot.dataset.caption || "";
			box.showModal();
		});
	});

	closeBtn.addEventListener("click", () => {
		box.close();
	});

	// Clicking the backdrop (i.e. the dialog element itself) closes it.
	box.addEventListener("click", (e) => {
		if (e.target === box) box.close();
	});

	box.addEventListener("close", () => {
		img.src = "";
	});
})();
