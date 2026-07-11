        # .texOffs(0, 0).addBox(-8, -3, -3, 16, 6, 6)

def genCode(texs, boxSizes):
    for i, (tex, boxSize) in enumerate(zip(texs, boxSizes)):
        print(f".texOffs({tex[0]},{tex[1]}).addBox(-{int(boxSize[0] / 2)},-{int(boxSize[1] / 2)},-{int(boxSize[2] / 2)},{boxSize[0]},{boxSize[1]},{boxSize[2]}, new CubeDeformation({0.001 * i}f))")