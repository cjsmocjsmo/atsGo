for f in /home/charliepi/go/atsGo/static/gallery/portrait/*.jpg; do
cwebp -q 95 "$f" -o "${f%.jpg}.webp"
done

for f in /home/charliepi/go/atsGo/static/gallery/portrait/*.jpg; do
cwebp -q 95 -resize 300 0 "$f" -o "${f%.jpg}_thumb.webp"
done