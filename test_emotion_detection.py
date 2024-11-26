from EmotionDetection.emotion_detection import emotion_detector
import  unittest  
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_check(self):
        self.assertEqual(emotion_detector("I'm glad that happened")['dominant_emotion'],'joy')
        self.assertEqual(emotion_detector("I was very angry about it")['dominant_emotion'],'anger')
        self.assertEqual(emotion_detector("Just hearing that disgusts me")['dominant_emotion'],'disgust')
        self.assertEqual(emotion_detector("I feel very sad about this")['dominant_emotion'],'sadness')
        self.assertEqual(emotion_detector("I'm really scared this is going to happen")['dominant_emotion'],'fear')

if __name__ == '__main__':
    unittest.main()