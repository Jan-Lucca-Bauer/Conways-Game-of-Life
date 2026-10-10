# Conway's Game of Life : Rules

<table border="1" width="600" frame="box">
    <thead>
        <tr>
            <th width="70%">Rule</th>
            <th width="30%">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <strong>1. Survival</strong><br><br>
                A living cell lives also in the next generation if it has 2 or 3 living neighbors.
                <br><br>
                In the example, the living cell in the middle has exactly 2 living neighbors and will stay alive in the next generation.
            </td>
            <td align="center">
                ⬜⬜🟩<br>
                ⬜🔳⬜<br>
                ⬜⬜🟩
            </td>
        </tr>
        <tr>
            <td>
                <strong>2. Reproduction</strong><br><br>
                A dead cell lives in the next generation if it has exactly 3 living neighbors.
                <br><br>
                In the example, the dead cell in the middle has exactly 3 living neighbors and will live in the next generation.
            </td>
            <td align="center">
                ⬜⬜⬜<br>
                🟩🔳⬜<br>
                ⬜🟩🟩
            </td>
        </tr>
        <tr>
            <td>
                <strong>3. Underpopulation</strong><br><br>
                A living cell dies in the next generation if it has less than 2 living neighbors.
                <br><br>
                In the example, the living cell in the middle has only 1 living neighbor and will die in the next generation.
            </td>
            <td align="center">
                ⬜🟩⬜<br>
                ⬜🔳⬜<br>
                ⬜⬜⬜
            </td>
        </tr>
        <tr>
            <td>
                <strong>4. Overpopulation</strong><br><br>
                A living cell dies in the next generation if it has more than 3 living neighbors.
                <br><br>
                In the example, the living cell in the middle has 4 living neighbors and will die in the next generation.
            </td>
            <td align="center">
                🟩⬜🟩<br>
                ⬜🔳⬜<br>
                🟩⬜🟩
            </td>
        </tr>
    </tbody>
</table>