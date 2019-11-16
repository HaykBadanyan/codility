def solution(H):
    count = 0
    rects = []
    for h in H:
        if not rects:
            rects.append(h)
            count += 1
        else:
            rect = rects.pop()
            if h > rect:
                rects.append(rect)
                rects.append(h)
                count += 1
            elif h == rect:
                rects.append(rect)
            else:
                while rects:
                    rect = rects.pop()
                    if rect == h:
                        rects.append(rect)
                        break
                    elif h > rect:
                        rects.append(rect)
                        rects.append(h)
                        count += 1
                        break
                else:
                    rects.append(h)
                    count += 1
    return count
