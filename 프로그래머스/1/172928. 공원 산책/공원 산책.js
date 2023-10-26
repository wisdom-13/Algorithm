function solution(park, routes) {
    
    park = park.map((item) => [...item]);
    routes = routes.map((item) => item.split(' '));
    
    const index = park.flat().indexOf("S");
    let [posX, posY] = [~~(index / park[0].length), index % park[0].length];
    
    for (i = 0; i < routes.length; i++) {
        const move = Number(routes[i][1]);
        let error = false;
        
        switch(routes[i][0]) {
            case "N":
                for (j = posX-1; j >= posX - move; j--) {
                   
                    
                    if (j < 0 || park[j][posY] == "X") {
                        error = true;
                        continue
                    };
                   
                    
                }
                posX = (error) ? posX : posX - move;
            break;
            
            case "S":
                for (j = posX+1; j <= posX + move; j++) {
                    if (j > park.length - 1 || park[j][posY] == "X") {
                        error = true;
                        continue
                    }
                }
                posX = (error) ? posX : posX + move;
            break;
                
            case "W":
                for (j = posY-1; j >= posY - move; j--) {
                    if (!park[posX][j] || park[posX][j] == "X") {
                        error = true;
                        continue
                    }
                }

                posY = (error) ? posY : posY - move;
            break;
                
            case "E":
                for (j = posY+1; j <= posY + move; j++) {
                    if (!park[posX][j] || park[posX][j] == "X") {
                        error = true;
                        continue
                    }
                }
                posY = (error) ? posY : posY + move;
            break;
        }
    }
    
    return [posX, posY];
}