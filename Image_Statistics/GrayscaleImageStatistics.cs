using System;
using System.IO;

public class GrayscaleImageStatistics
{
    private byte[] _pixels;
    private int _width;
    private int _height;

    public double Mean { get; private set; }
    public double StdDev { get; private set; }
    public byte Min { get; private set; }
    public byte Max { get; private set; }

    public GrayscaleImageStatistics(string imagePath)
    {
        // Load the image from file
        using (FileStream stream = new FileStream(imagePath, FileMode.Open))
        {
            using (BinaryReader reader = new BinaryReader(stream))
            {
                // Read the image dimensions
                _width = reader.ReadInt32();
                _height = reader.ReadInt32();

                // Read the pixel values into an array
                _pixels = new byte[_width * _height];
                for (int i = 0; i < _pixels.Length; i++)
                {
                    _pixels[i] = reader.ReadByte();
                }
            }
        }

        // Calculate the statistics
        CalculateStatistics();
    }

    private void CalculateStatistics()
    {
        // Calculate the mean
        double sum = 0.0;
        foreach (byte pixel in _pixels)
        {
            sum += pixel;
        }
        Mean = sum / _pixels.Length;

        // Calculate the standard deviation
        double sumOfSquares = 0.0;
        foreach (byte pixel in _pixels)
        {
            double diff = pixel - Mean;
            sumOfSquares += diff * diff;
        }
        StdDev = Math.Sqrt(sumOfSquares / _pixels.Length);

        // Find the minimum and maximum pixel values
        Min = byte.MaxValue;
        Max = byte.MinValue;
        foreach (byte pixel in _pixels)
        {
            if (pixel < Min) Min = pixel;
            if (pixel > Max) Max = pixel;
        }
    }
}
