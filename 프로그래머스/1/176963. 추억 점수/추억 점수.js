function solution(name, yearning, photo) {
    var score = {};
    
    for (i in name) {
        score[name[i]] = yearning[i]
    }
    
    photo = photo.map(
        (item) => item.map((i) => score[i] ? score[i] : 0).reduce((a, b) => a + b)
    )
    
    return photo;
}