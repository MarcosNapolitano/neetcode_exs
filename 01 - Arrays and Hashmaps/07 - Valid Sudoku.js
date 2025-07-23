/**
 * @param {character[][]} board
 * @return {boolean}
 */
     
var isValidSudoku = function (board) {
    let result = true;
    let sector = 1;
    let index = new Map();

    //recopilamos coordenadas
    //sector, hor, ver

    board.map((a, b) => {
        for (let i in a) {
            //routeado basico de sectores, y reseteo
            switch (b) {
                case 0:
                case 1:
                case 2:
                    if (i == "0") sector = 1;
                    break;
                case 3:
                case 4:
                case 5:
                    if (i == "0") sector = 4;
                    break;
                case 6:
                case 7:
                case 8:
                    if (i == "0") sector = 7;
                    break;
            }

            if (i == "3") sector++;
            if (i == "6") sector++;

            if (a[i] == ".") continue;
            //+ 1 porque arrancan en 0
            //la idea es separar en 3 array uno por cada coordenada para luego filtar repetidos
            if (index.get(a[i])) {
                index.get(a[i])[0].push(sector);
                index.get(a[i])[1].push(parseInt(i) + 1);
                index.get(a[i])[2].push(b + 1);
            } else index.set(a[i], [[sector], [parseInt(i) + 1], [b + 1]]);
        }
    });

    const results = [...index.values()];

    for (let i in results) {
        for (let j in results[i]) {
            index = new Map();
            results[i][j].map((a) => {
                if (index.get(a)) result = false;
                else index.set(a, 1);
            });
            if (!result) break;
        }
        if (!result) break;
    }
    return result;
};
