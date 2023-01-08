import requests
from bs4 import BeautifulSoup
import draftPredictor


def get_data(url, pos, all_star, all_nba):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div_totals = soup.find("div", {"id": "div_totals"})
    div_college = soup.find("div", {"id": "all_all_college_stats"})
    totals = get_totals(div_totals)
    college = get_college(div_college)

    return draftPredictor.Player(pos,
                                 college[0], college[1], college[2], college[3], college[4], college[5],
                                 totals[0], totals[1], totals[2], totals[3], totals[4],
                                 all_star, all_nba)



def get_totals(div):
    footer = div.find('tfoot')
    tr = footer.find('tr')
    pts = tr.prettify().split('<td class="right" data-stat="pts">')
    points = pts[1][3:len(pts[1]) - 13]
    print(float(points))
    try:
        trash = pts[0].split('<td class="right" data-stat="tov">')
        blk = trash[0].split('<td class="right" data-stat="blk">')
        blocks = blk[1][:len(blk[1]) - 7]
        print(float(blocks))
    except ValueError:
        trash = pts[0].split('<td class="right iz" data-stat="tov">')
        blk = trash[0].split('<td class="right" data-stat="blk">')
        blocks = blk[1][:len(blk[1]) - 7]
        print(float(blocks))
    except IndexError:
        blk = trash[0].split('<td class="right iz" data-stat="blk">')
        blocks = blk[1][:len(blk[1]) - 7]
        print(float(blocks))
    stl = blk[0].split('<td class="right" data-stat="stl">')
    steals = stl[1][:len(stl[1]) - 7]
    print(float(steals))
    ast = stl[0].split('<td class="right" data-stat="ast">')
    assists = ast[1][:len(ast[1]) - 7]
    print(float(assists))
    trb = ast[0].split('<td class="right" data-stat="trb">')
    rebounds = trb[1][:len(trb[1]) - 7]
    print(float(rebounds))
    return [float(points), float(rebounds), float(assists), float(steals), float(blocks)]


def get_college(div):
    tfoot = div.prettify().split("<tfoot>")
    end_out = tfoot[1].split("</tr>")
    ast = end_out[0].split('<td class="right " data-stat="ast_per_g" >')
    assists = ast[1][:len(ast[1])-5]
    print(float(assists))
    trb = ast[0].split('<td class="right " data-stat="trb_per_g" >')
    rebounds = trb[1][:len(trb[1])-5]
    print(float(rebounds))
    pts = trb[0].split('<td class="right " data-stat="pts_per_g" >')
    points = pts[1][:len(pts[1])-5]
    print(float(points))
    fg = pts[0].split('<td class="right " data-stat="fg_pct" >')
    fg_pct = fg[1][:len(pts[1])-5]
    print(float(fg_pct))
    trash = fg[0].split('<td class="right " data-stat="tov" >')
    blk = trash[0].split('<td class="right " data-stat="blk" >')
    blocks = blk[1][:len(blk[1])-5]
    print(float(blocks))
    stl = blk[0].split('<td class="right " data-stat="stl" >')
    steals = stl[1][:len(stl[1])-5]
    print(float(steals))
    more_trash = stl[0].split('<td class="right " data-stat="mp" >')
    g = more_trash[0].split('<td class="right " data-stat="g" >')
    games = g[1][:len(ast[1])-6]
    print(float(games))

    return [float(points), float(rebounds), float(assists), float(fg_pct),
            float(steals)/float(games), float(blocks)/float(games)]

