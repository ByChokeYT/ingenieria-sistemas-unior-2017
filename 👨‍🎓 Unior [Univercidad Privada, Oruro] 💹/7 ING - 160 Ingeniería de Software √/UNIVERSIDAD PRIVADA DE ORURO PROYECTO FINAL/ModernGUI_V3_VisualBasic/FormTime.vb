Public Class FormTime
    Private Sub Horafecha_Tick(sender As Object, e As EventArgs) Handles Horafecha.Tick

        iblhora.Text = DateTime.Now.ToLongTimeString()
        iblfecha.Text = DateTime.Now.ToString("dddd:MMMM:yyy")

    End Sub

    Private Sub Label2_Click(sender As Object, e As EventArgs) Handles iblfecha.Click

    End Sub

    Private Sub PictureBox1_Click(sender As Object, e As EventArgs) Handles PictureBox1.Click
        Me.Close()
    End Sub
End Class