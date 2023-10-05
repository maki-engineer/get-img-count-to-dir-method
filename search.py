import os


def get_img_count_to_dir(
        directory_path: str,
        image_count: int = 0,
        image_extensions: list = ['.jpg', '.jpeg', '.png', '.gif']) -> int:
    """指定したパス内の画像数を返す。

    Args:
        directory_path (str): パス
        image_count (int): 画像数
        image_extensions (str): 検索したい拡張子リスト

    Returns:
        int: 画像数。
    """

    # ファイルを取得
    files = os.listdir(directory_path)

    # 画像とフォルダを取得
    imgs = []
    folders = []
    for f in files:
        if os.path.isfile(os.path.join(directory_path, f)) and any(f.endswith(ext) for ext in image_extensions):
            imgs.append(f)

        if os.path.isdir(os.path.join(directory_path, f)):
            folders.append(f)

    # print(f"ディレクトリ: {directory_path}, 画像数: {len(imgs)}")
    image_count = len(imgs)

    if len(folders) != 0:
        for f in folders:
            image_count += get_img_count_to_dir(os.path.join(directory_path, f))

    return image_count


directory_path = ''

print(get_img_count_to_dir(directory_path))
